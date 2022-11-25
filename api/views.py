from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import *
from api.pagination import SmallMediumPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from api.renderers import UserRenderer

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.filter().order_by('pk')
    serializer_class = UserSerializer
    authentication_class = [TokenObtainPairView]
    permission_class = (IsAuthenticated,)


class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    authentication_class = [TokenObtainPairView]
    permission_classes = (IsAuthenticated,)


class EssayListCreate(generics.ListCreateAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer
    permission_classes = [IsAuthenticated, ]


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer
    permission_classes = [IsAuthenticated, ]


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]

class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]


class EssayQuestionsAlternativeAll(generics.RetrieveUpdateAPIView):
    queryset = Essay.objects.filter(is_deleted=False).order_by('pk')
    serializer_class = EssayQuestionsAlternativeAllSerializer
    permission_classes = [IsAuthenticated, ]


class RegistrationView(APIView):
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
            return Response({'token': token, 'msg': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Email o contraseña invalidos']}},
                            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'msg': 'Se cerro la sesión con éxito'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(APIView):
  renderer_classes = [UserRenderer,]
  permission_classes = [IsAuthenticated, ]

  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
