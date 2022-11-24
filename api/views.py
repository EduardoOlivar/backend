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

# Create your views here.


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


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class EssayQuestionsAlternativeAll(generics.RetrieveUpdateAPIView):
    queryset = Essay.objects.filter(is_deleted=False).order_by('pk')
    serializer_class = EssayQuestionsAlternativeAllSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Faltan credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Inicio de sesión exitoso', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


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


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }