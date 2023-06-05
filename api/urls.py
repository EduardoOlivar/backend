from api import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework_simplejwt import views as jwt_views


# RESTful endpoints
urlpatterns = [
    re_path(r'^user(s)?/all/$', views.UsersListCreate.as_view()),  # Endpoint para consultar listado de usuarios
    re_path(r'^user(s)?/(?P<pk>[0-9]+)/$', views.UsersRetrieveUpdateDestroy.as_view()),  # Endpoint para consultar, eliminar, actualizar un usuario específico
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obtener un token
    re_path('api/register/', views.RegisterView.as_view(), name='register'),  # Endpoint para registrar usuario
    re_path('api/login/', views.LoginView.as_view(), name='login'),  # Endpoint para iniciar sesión
    re_path('api/logout/', views.LogoutView.as_view(), name='logout'),  # Endpoint para cerrar sesión
    re_path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para refrescar el token

    re_path(r'^essays/list/all/$', views.EssayList.as_view()),  # Endpoint para consultar todos los tipos de ensayos
    re_path(r'^essays/create/$', views.EssayCreate.as_view()),  # Endpoint para crear un ensayo
    re_path(r'^essays/(?P<pk>[0-9]+)/$', views.EssayRetrieveUpdateDestroy.as_view()),  # Endpoint para consultar, eliminar, actualizar un ensayo específico

    re_path(r'^questions/list/all/$', views.QuestionList.as_view()),  # Endpoint para consultar todas las preguntas
    re_path(r'^questions/create/$', views.QuestionCreate.as_view()),  # Endpoint para crear una pregunta
    re_path(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionRetrieveUpdateDestroy.as_view()),  # Endpoint para consultar, eliminar, actualizar una pregunta específica

    re_path(r'^answers/list/all/$', views.AnswerList.as_view()),  # Endpoint para consultar todas las respuestas
    re_path(r'^answers/create/$', views.AnswerCreate.as_view()),  # Endpoint para crear una respuesta
    re_path(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerRetrieveUpdateDestroy.as_view()),  # Endpoint para consultar, eliminar, actualizar una respuesta específica

    re_path(r'^questions_alternative/$', views.QuestionsAlternativeAllView.as_view()),  # Endpoint para consultar todas las preguntas y alternativas de un ensayo específico
    re_path(r'^score_user/all/$', views.AnswerEssayUserView.as_view()),  # Endpoint para obtener el puntaje del usuario
    re_path(r'^submit_essay_user/$', views.UserEssayView.as_view()),  # Endpoint para guardar el ensayo realizado por el usuario
    re_path(r'^submit_answers/$', views.SaveAnswersView.as_view()),  # Endpoint para guardar las respuestas del usuario
    re_path(r'^history/(?P<pk>[0-9]+)/$', views.UserEssayHistoryView.as_view()),  # Endpoint para consultar el historial de ensayos de un usuario
    re_path(r'^custom_essays/$', views.CustomEssayView.as_view()),  # Endpoint para consultar y crear ensayos personalizados
    re_path(r'^custom_essay_questions/$', views.CustomEssayQuestionView.as_view()),  # Endpoint para asociar preguntas a un ensayo personalizado
]

urlpatterns += [
    re_path(r'^api/send_reset_password_email/$', views.SendPasswordResetEmailView.as_view(), name='send_reset_password_email'),#endpoint para pedir un cambio de contraseña via mail
    path('api/reset_password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset_password'),#endpoint para cambiar la contraseña si se tiene uid y el token asignado
    re_path(r'^api/change_password/$', views.ChangePasswordView.as_view(), name='change_password'),#endpoint para cambiar la contraseña
    re_path(r'^api/profile/$', views.UserProfileView.as_view(), name='profile'),#endpoint para consultar el perfil del usuario

]

