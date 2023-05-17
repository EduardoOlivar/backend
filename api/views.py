from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout
from api.renderers import UserRenderer
from django_filters.rest_framework import DjangoFilterBackend
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

#funcion para obtener jwt para el usuario cuando hace login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#views para el manejo de los user

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.filter().order_by('pk')
    serializer_class = UserSerializer


class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Inicio de sesión exitoso','status': 'ok'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Email o contraseña invalidos']}},
                            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'msg': 'Se cerro la sesión con éxito'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def patch(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Contraseña cambiada exitosamente'}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer,]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Link para reiniciar contraseña enviado'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Cambio de contraseña exitoso'}, status=status.HTTP_200_OK)


#demas views
class EssayList(generics.ListAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class EssayCreate(generics.CreateAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionCreateSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','essays', 'question','subject','link_resolution']


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerCreateSerializer


class QuestionsAlternativeAllView(generics.ListAPIView):
    serializer_class = QuestionsAlternativeAllSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','essays','subject']
    queryset = Question.objects.all()


class AnswerEssayUserView(generics.ListAPIView):
    serializer_class = AnswerEssayUserSerializer
    queryset = AnswerEssayUser.objects.filter(is_deleted=False).order_by('pk')


class UserEssayView(generics.CreateAPIView):
    serializer_class = EssayUserSerializer
    queryset = UserEssay.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaveAnswersView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveAnswersSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)


class UserEssayHistoryView(generics.ListAPIView):
    serializer_class = UserEssayHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_pk = self.kwargs['pk']
        return UserEssay.objects.filter(user_id=user_pk)