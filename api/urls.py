from api import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework_simplejwt import views as jwt_views


# RESTful endpoints
urlpatterns = [
    re_path(r'^user(s)?/all/$', views.UsersListCreate.as_view()), #endpoint para consultar listado de usuarios
    re_path(r'^user(s)?/(?P<pk>[0-9]+)/$', views.UsersRetrieveUpdateDestroy.as_view()),#endpoint para consultar usuario especifico, eliminarlo ,recuperarlo o updatearlo
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#endpoint para obtener un token
    re_path('api/register/', views.RegisterView.as_view(), name='register'),#endpoint para registrar usuario
    re_path('api/login/', views.LoginView.as_view(), name='login'),#endpoint para iniciar sesion
    re_path('api/logout/', views.LogoutView.as_view(), name='logout'),#endpoint desconexion
    re_path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),#endpoint para refresh token
    re_path(r'^essays/list/all/$', views.EssayList.as_view()), #endpoint para consultar todos los tipos de ensayos
    re_path(r'^essays/create/$', views.EssayCreate.as_view()),
    re_path(r'^essays/(?P<pk>[0-9]+)/$', views.EssayRetrieveUpdateDestroy.as_view()), #endpoint para consultar por un ensayo en especifico, solo muestra los atributos de ensayo, se puede aplicar crud
    re_path(r'^questions/list/all/$', views.QuestionList.as_view()),
    re_path(r'^questions/create/$', views.QuestionCreate.as_view()),
    re_path(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionRetrieveUpdateDestroy.as_view()),
    re_path(r'^answers/list/all/$', views.AnswerList.as_view()),
    re_path(r'^answers/create/$', views.AnswerCreate.as_view()),
    re_path(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerRetrieveUpdateDestroy.as_view()),
    re_path(r'^questions_alternative/$', views.QuestionsAlternativeAllView.as_view()),#endpoint para consultar por un ensayo en especifico con todas sus  preguntas y alternativas
    re_path(r'^score_user/all/$', views.AnswerEssayUserView.as_view()), #endpoint para obtener el puntaje del usuario
    re_path(r'^submit_essay_user/$', views.UserEssayView.as_view()), #endpoint que guarda el ensayo que realizo el usuario
    re_path(r'^submit_answers/$', views.SaveAnswersView.as_view()),#endpoint para guardar las respuestas del usuario
    re_path(r'^history/(?P<pk>[0-9]+)/$', views.UserEssayHistoryView.as_view()) # endpoint para el historial
]

urlpatterns += [
    re_path(r'^api/send_reset_password_email/$', views.SendPasswordResetEmailView.as_view(), name='send_reset_password_email'),#endpoint para pedir un cambio de contraseña via mail
    path('api/reset_password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset_password'),#endpoint para ccambiar la contraseña si se tiene uid y el token asignado
    re_path(r'^api/change_password/$', views.ChangePasswordView.as_view(), name='change_password'),#endpoint para cambiar la contraseña
    re_path(r'^api/profile/$', views.UserProfileView.as_view(), name='profile'),#endpoint para consultar el perfil del usuario

]

