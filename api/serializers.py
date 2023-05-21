from api.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, get_connection
from backend.settings import EMAIL_HOST_USER

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
    username = serializers.CharField(max_length=255)

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
            # Envia email
            subject = 'Reinicia tu contraseña'
            message = f'Presiona el siguiente link para reiniciar tu contraseña: {link}/'
            from_email = EMAIL_HOST_USER
            recipient_list = [email]
            connection = get_connection()
            connection.open()
            send_mail(subject,message,from_email,recipient_list)
            connection.close()
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
        exclude = [*generic_fields, 'questions', 'users', 'essay']


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = [*generic_fields, 'users']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields, 'essays']


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
        fields = ['essays', 'score', 'answers']


#serializador para mostrar las respuestas y sus preguntas ademas de la id el ensayo
class QuestionsAlternativeAllSerializer(QuestionSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    def to_representation(self, instance: Question):
        data = super().to_representation(instance)
        essay = instance.essays
        data['essay'] = essay.id
        return data


class EssayQuestionsAlternativeAllSerializer(EssaySerializer):
    question = QuestionsAlternativeAllSerializer(many=True, read_only=True)


#serializador para crear una id unica cuando se crea un ensayo para un usuario
class EssayUserSerializer(serializers.Serializer):
    essay_id = serializers.IntegerField()

    class Meta:
        model = UserEssay
        exclude = [*generic_fields]

    def to_representation(self, instance:UserEssay):
        data = super().to_representation(instance)
        del data['essay_id']
        data['new_id'] = instance.id
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        essay_id = validated_data.get('essay_id')
        essay = Essay.objects.get(id=essay_id)
        user_essay = UserEssay.objects.create(user=user, essay=essay)
        return user_essay


#serializador que guarda las respuestas de un ensayo creado para un usuario
class SaveAnswersSerializer(serializers.Serializer):
    answer_ids = serializers.ListSerializer(child=serializers.IntegerField())
    user_essay_id = serializers.IntegerField()
    time_essay = serializers.CharField()

    def validate(self, value):
        answer_ids = value.get('answer_ids')
        user_essay_id = value.get('user_essay_id')
        user_essay = get_object_or_404(UserEssay, pk=user_essay_id)
        answers = Answer.objects.filter(id__in=answer_ids, questions__essays=user_essay.essay)
        if len(answer_ids) != len(answers):
            raise serializers.ValidationError('respuestas no validas')
        return value

    def create(self, validated_data):
        answer_ids = validated_data.get('answer_ids')
        time_essay = validated_data.get('time_essay')
        user_essay_id = validated_data.get('user_essay_id')
        user_essay = UserEssay.objects.get(pk=user_essay_id)
        user = self.context['request'].user
        for answer_id in answer_ids:
            answer = Answer.objects.get(pk=answer_id)
            if AnswerEssayUser.objects.filter(answers=answer, essays=user_essay).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de UserEssay y Answer')
            essay_answers = AnswerEssayUser.objects.create(answers=answer, essays=user_essay, users=user, score=answer.right, time_essay=time_essay)
        return essay_answers


class UserEssayHistorySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = UserEssay
        exclude = [*generic_fields, 'user','essay']

    def get_custom(self, instance):
        if not instance.essay.is_custom:
            return "No"
        return "Si"

    def get_date(self, instance):
        return instance.created.date()

    def get_questions(self, instance):
        return instance.essay.question.count()

    def get_score(self, instance):
        questions = self.get_questions(instance)
        if questions == 0:
            return 0
        answers = AnswerEssayUser.objects.filter(essays=instance)
        right = 0
        for answer in answers:
            if answer.score == 1:
                right = right + 1

        score = 100 + (900 / questions) * right
        return round(score)

    def get_time_essay(self,instance):
        answer_essay_user = instance.answers_essay_user.first()
        if answer_essay_user:
            return answer_essay_user.time_essay
        else:
            return None

    def to_representation(self, instance: UserEssay):
        data = super().to_representation(instance)
        data['name'] = instance.essay.name
        data['is_custom'] = self.get_custom(instance)
        data['questions'] = self.get_questions(instance)
        data['time'] = self.get_time_essay(instance)
        data['puntaje'] = self.get_score(instance)
        return data




# filtros por fecha, por puntaje, por tema
