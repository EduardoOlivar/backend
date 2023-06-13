from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout
from api.renderers import UserRenderer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

#funcion para obtener jwt para el usuario cuando hace login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)  # Genera un token de actualización para el usuario proporcionado

    return {
        'refresh': str(refresh),  # Convierte el token de actualización a una cadena y lo retorna
        'access': str(refresh.access_token),  # Convierte el token de acceso asociado al token de actualización a una cadena y lo retorna
    }


# Views para el manejo de usuarios

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.filter().order_by('pk')  # Obtiene todos los usuarios ordenados por su clave primaria
    serializer_class = UserSerializer  # Serializador utilizado para la representación de los usuarios


class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()  # Obtiene todos los usuarios
    serializer_class = UserSerializer  # Serializador utilizado para la representación de los usuarios

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        if serializer.is_valid():
            serializer.save()  # Guarda los datos del nuevo usuario en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna los datos del usuario registrado en la respuesta con un código de estado 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna los errores de validación en la respuesta con un código de estado 400 (BAD REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        email = serializer.data.get('email')  # Obtiene el email del usuario del serializador
        password = serializer.data.get('password')  # Obtiene la contraseña del usuario del serializador
        user = authenticate(email=email, password=password)  # Autentica al usuario utilizando el email y la contraseña
        if user is not None:
            token = get_tokens_for_user(user)  # Obtiene el token de acceso para el usuario autenticado
            return Response({'token': token, 'msg': 'Inicio de sesión exitoso', 'status': 'ok','user_id':user.id}, status=status.HTTP_200_OK)  # Retorna el token de acceso en la respuesta con un mensaje de éxito y un código de estado 200 (OK)
        else:
            return Response({'errors': {'error_de_campo': ['Email o contraseña invalidos']}}, status=status.HTTP_404_NOT_FOUND)  # Retorna un mensaje de error en la respuesta con un código de estado 404 (NOT FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)  # Cierra la sesión del usuario
        return Response({'msg': 'Se cerro la sesión con éxito'},
                        status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def patch(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data, context={
            'user': request.user})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Contraseña cambiada exitosamente'},
                        status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class UserProfileView(APIView):
    renderer_classes = [UserRenderer,]  # Clase de renderizado utilizada para la vista
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)  # Serializador utilizado para convertir el objeto de usuario en datos JSON
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna los datos del usuario en la respuesta


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Link para reiniciar contraseña enviado'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg':'Cambio de contraseña exitoso'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class EssayList(generics.ListAPIView):
    queryset = Essay.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class EssayCreate(generics.CreateAPIView):
    queryset = Essay.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Essay.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionCreateSerializer  # Clase serializadora utilizada


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()  # Consulta para obtener todas las preguntas
    serializer_class = QuestionSerializer  # Clase serializadora utilizada

    filter_backends = [DjangoFilterBackend]  # Filtros aplicados a la vista
    filterset_fields = ['id', 'essays', 'question', 'subject', 'link_resolution']  # Campos permitidos para filtrar


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionSerializer  # Clase serializadora utilizada


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerSerializer  # Clase serializadora utilizada


class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerSerializer  # Clase serializadora utilizada


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerCreateSerializer  # Clase serializadora utilizada


class QuestionsAlternativeAllView(generics.ListAPIView):
    serializer_class = QuestionsAlternativeAllSerializer  # Clase serializadora utilizada
    filter_backends = [DjangoFilterBackend]  # Filtros aplicados a la vista
    filterset_fields = ['id', 'essays', 'subject']  # Campos permitidos para filtrar
    queryset = Question.objects.all()  # Consulta para obtener todas las preguntas


class AnswerEssayUserView(generics.ListAPIView):
    serializer_class = AnswerEssayUserSerializer  # Clase serializadora utilizada
    queryset = AnswerEssayUser.objects.filter(is_deleted=False).order_by('pk')  # Consulta para obtener las respuestas de los ensayos de usuario no eliminadas, ordenadas por clave primaria


class SaveAnswersView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista
    serializer_class = SaveAnswersSerializer  # Clase serializadora utilizada

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})  # Crear una instancia del serializador con los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Validar los datos y lanzar una excepción en caso de que sean inválidos
        serializer.save()  # Guardar los datos
        return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa


class UserEssayHistoryView(generics.ListAPIView):
    serializer_class = UserEssayHistorySerializer  # Clase serializadora utilizada
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista

    def get_queryset(self):
        user_pk = self.kwargs['pk']  # Obtener el ID del usuario de los parámetros de la URL
        return CustomEssay.objects.filter(user_id=user_pk)  # Devolver los ensayos personalizados del usuario


class CustomEssayView(generics.CreateAPIView):
    queryset = CustomEssay.objects.filter(is_deleted=False)  # Consulta para obtener los ensayos personalizados que no han sido eliminados
    serializer_class = CustomEssaySerializer  # Clase serializadora utilizada

    def perform_create(self, serializer):
        custom_essay = serializer.save()  # Guardar el ensayo personalizado
        response_data = {'id': custom_essay.id, 'message': 'CustomEssay creado exitosamente.'}
        return Response(response_data, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa


class CustomEssayQuestionView(generics.ListCreateAPIView):
    queryset = CustomEssayQuestion.objects.filter(is_deleted=False)  # Consulta para obtener las relaciones entre ensayos personalizados y preguntas que no han sido eliminadas
    serializer_class = CustomEssayQuestionSerializer  # Clase serializadora utilizada
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista

