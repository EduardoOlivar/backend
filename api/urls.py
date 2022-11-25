from api import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework_simplejwt import views as jwt_views


# RESTful endpoints
urlpatterns = [
    re_path(r'^user(s)?/all/$', views.UsersListCreate.as_view()),
    re_path(r'^user(s)?/(?P<pk>[0-9]+)/$', views.UsersRetrieveUpdateDestroy.as_view()),
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/register/', views.RegistrationView.as_view(), name='register'),
    re_path('api/login/', views.LoginView.as_view(), name='login'),
    re_path('api/logout/', views.LogoutView.as_view(), name='logout'),
    re_path('api/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    re_path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('api/profile/', views.UserProfileView.as_view(), name='profile'),
]


urlpatterns += [
    re_path(r'^essays/all/$', views.EssayListCreate.as_view()), #endpoint para consultar todos los tipos de ensayos
    re_path(r'^essays/(?P<pk>[0-9]+)/$', views.EssayRetrieveUpdateDestroy.as_view()), #endpoint para consultar por un ensayo en especifico, solo muestra los atributos de ensayo
    re_path(r'^questions/all/$', views.QuestionListCreate.as_view()),
    re_path(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionRetrieveUpdateDestroy.as_view()),
    re_path(r'^answers/all/$', views.AnswerListCreate.as_view()),
    re_path(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerRetrieveUpdateDestroy.as_view()),
    re_path(r'^essay_questions_alternative/(?P<pk>[0-9]+)/$', views.EssayQuestionsAlternativeAll.as_view()),#endpoint para consultar por un ensayo en especifico con todas sus  preguntas y alternativas
]
