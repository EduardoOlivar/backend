from api.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.shortcuts import get_object_or_404

generic_fields = ['created', 'updated', 'is_deleted']


#serializadores para class user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = [*generic_fields,'is_admin']


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Users
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username']


#serializador para el registro del usuario, compara las contraseñas para el match

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Users(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Las contraseñas deben coincidir.'})
        user.set_password(password)
        user.save()
        return user


#cambia la contraseña solo si se sabe la contraseña actual
class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('Link para reiniciar contraseña', link)
            # # Envia email
            body = 'Presiona el siguiente link para reiniciar tu contraseña'+link
            data = {
            'subject':'Reinicia tu contraseña',
            'body':body,
            'to_email':user.email
            }
            # Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('No eres un usuario registrado')


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Las contraseñas no coinciden")
            id = smart_str(urlsafe_base64_decode(uid))
            user = Users.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('El token no es valido o expiro')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('El token no es valido o expiro')


#demas serializers

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = [*generic_fields, 'question', 'users', 'essay']


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = [*generic_fields, 'users']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields, 'essay']


class QuestionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields]


class EssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Essay
        exclude = [*generic_fields, 'users']


class AnswerEssayUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerEssayUser
        fields = ['essay', 'score', 'answer']


class QuestionsAlternativeAllSerializer(QuestionSerializer):
    answer = AnswerSerializer(many=True, read_only=True)


class EssayQuestionsAlternativeAllSerializer(EssaySerializer):
    question = QuestionsAlternativeAllSerializer(many=True, read_only=True)


class SaveAnswersSerializer(serializers.Serializer):
    answer_ids = serializers.ListSerializer(child=serializers.IntegerField())
    essay_id = serializers.IntegerField()

    def validate(self, value):
        essay_id = value.get('essay_id')
        answer_ids = value.get('answers_id')
        essay = get_object_or_404(Essay, pk=essay_id)
        answers = Answer.objects.filter(id__in=answer_ids, questions__essay__id=essay_id)
        if len(answer_ids) != len(answers):
            raise serializers.ValidationError('respuestas no validas')
        return value

    def create(self, validated_data):
        answers_ids = validated_data.get('answers_ids')
        essay_id = validated_data.get('essay_id')
        user = self.context['request'].user
        for answer_id in answers_ids:
            answer = Answer.objects.get(pk=answer_id)
            essay_answers = AnswerEssayUser.objects.create(answer=answer, essay=essay_id, users=user, score=answer.right)
        return essay_answers
