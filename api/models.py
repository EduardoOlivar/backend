import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import timedelta
from datetime import time
from django.utils import timezone
# Create your models here.
common_args = {'null': True, 'blank': True} #atributos generales que tienen que tener


class GenericAttributes(models.Model):
    created = models.DateTimeField(**common_args, auto_now_add=True, editable=False)  # para saber cuando fue creado el dato
    updated = models.DateTimeField(**common_args, auto_now=True) # para saber cuando se actualizo el dato
    is_deleted = models.BooleanField(**common_args, default=False) #para un borrado logico de las vistas no borrado fisico de la bd

    class Meta:
        abstract = True


# Create your models here
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser,GenericAttributes):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(**common_args,default=False)
    username = models.TextField(**common_args)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin


class Essay(GenericAttributes):
    name = models.TextField(**common_args)
    type = models.TextField(**common_args)
    is_custom = models.BooleanField(**common_args, default=False)
    users = models.ManyToManyField(Users, blank=True, through='UserEssay', related_name='essay')


class UserEssay(GenericAttributes):
    user = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='essay_user')
    essay = models.ForeignKey(Essay, **common_args, on_delete=models.CASCADE, related_name='user_essay')


class Question(GenericAttributes):
    question = models.TextField(**common_args)
    subject = models.TextField(**common_args)
    link_resolution = models.URLField(**common_args)
    essays = models.ForeignKey(Essay, **common_args,on_delete=models.CASCADE, related_name='question')


class Answer(GenericAttributes):
    label = models.CharField(**common_args, max_length=255)
    right = models.IntegerField(**common_args)
    questions = models.ForeignKey(Question, **common_args, on_delete=models.CASCADE, related_name='answer')
    users = models.ManyToManyField(Users, blank=True, through='AnswerEssayUser', related_name='answer')
    essay = models.ManyToManyField(UserEssay, blank=True, through='AnswerEssayUser', related_name='answer')


class AnswerEssayUser(GenericAttributes):
    answers = models.ForeignKey(Answer, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    essays = models.ForeignKey(UserEssay, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    users = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    score = models.IntegerField(**common_args)
    time_essay = models.TextField(**common_args)
