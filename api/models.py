import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
# Create your models here.
DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]


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
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
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
    users = models.ManyToManyField(Users, blank=True, related_name='essay')


class Question(GenericAttributes):
    question = models.TextField(**common_args)
    subject = models.TextField(**common_args)
    link_resolution = models.URLField(**common_args)
    essay = models.ForeignKey(Essay, **common_args,on_delete=models.CASCADE, related_name='question')


class Answer(GenericAttributes):
    label = models.CharField(**common_args, max_length=255)
    right = models.IntegerField(**common_args)
    question = models.ForeignKey(Question, **common_args, on_delete=models.CASCADE, related_name='answer')
    users = models.ManyToManyField(Users, blank=True, through='AnswerEssayUser', related_name='answer')
    essay = models.ManyToManyField(Essay, blank=True, through='AnswerEssayUser', related_name='answer')


class AnswerEssayUser(GenericAttributes):
    answer = models.ForeignKey(Answer,**common_args, on_delete=models.CASCADE)
    essay = models.ForeignKey(Essay,**common_args,on_delete=models.CASCADE)
    users = models.ForeignKey(Users,**common_args,on_delete=models.CASCADE)
    score = models.IntegerField(**common_args)
