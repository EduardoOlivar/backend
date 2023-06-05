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



#serializador que guarda las respuestas de un ensayo creado para un usuario
class SaveAnswersSerializer(serializers.Serializer):
    answer_ids = serializers.ListSerializer(child=serializers.IntegerField())
    user_essay_id = serializers.IntegerField()
    time_essay = serializers.CharField()

    def validate(self, data):
        answer_ids = data.get('answer_ids')
        user_essay_id = data.get('user_essay_id')
        time_essay = data.get('time_essay')

        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        answers = Answer.objects.filter(id__in=answer_ids, questions__essays__custom_essay=user_essay)
        print(user_essay)
        print(answers)
        print(answer_ids)
        if len(answer_ids) != len(answers):
            raise serializers.ValidationError('Respuestas no válidas.')

        return data

    def create(self, validated_data):
        answer_ids = validated_data.get('answer_ids')
        user_essay_id = validated_data.get('user_essay_id')
        time_essay = validated_data.get('time_essay')

        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        user = self.context['request'].user
        essay_answers = []

        for answer_id in answer_ids:
            answer = get_object_or_404(Answer, pk=answer_id)

            if AnswerEssayUser.objects.filter(answers=answer, essays=user_essay, users=user).exists():
                raise serializers.ValidationError(
                    'Ya existe una respuesta para esta combinación de UserEssay y Answer.')

            essay_answer = AnswerEssayUser.objects.create(answers=answer, essays=user_essay, users=user,
                                                          score=answer.right, time_essay=time_essay)
            essay_answers.append(essay_answer)

        return essay_answers


class UserEssayHistorySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = CustomEssay
        fields = ['name', 'is_custom', 'date']

    def get_date(self, instance):
        return instance.created.date()

    def get_questions(self, instance):
        return Question.objects.filter(essays__in=instance.essays.all()).count()

    def get_score(self, instance):
        questions = self.get_questions(instance)
        if questions == 0:
            return 0
        answers = AnswerEssayUser.objects.filter(essays=instance)
        right = answers.filter(score=1).count()
        score = 100 + (900 / questions) * right
        return round(score)

    def get_time(self, instance):
        answer_essay_user = instance.answers_essay_user.first()
        if answer_essay_user:
            return answer_essay_user.time_essay
        else:
            return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['questions'] = self.get_questions(instance)
        data['time_essay'] = self.get_time(instance)
        data['puntaje'] = self.get_score(instance)
        # Verificar si hay registros en AnswerEssayUser para el CustomEssay actual
        has_answer_essay_user = AnswerEssayUser.objects.filter(essays=instance).exists()
        if not has_answer_essay_user:
            # No mostrar el CustomEssay si no hay registros en AnswerEssayUser
            return None

        return data


class EssayAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssayAnswer
        fields = ['id']


class CustomEssaySerializer(serializers.ModelSerializer):
    essay_ids = serializers.ListField(write_only=True)
    essay_custom = EssayAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = CustomEssay
        fields = ('id', 'is_custom', 'name', 'essay_ids', 'essay_custom', 'user')

    def validate(self, attrs):
        essay_ids = attrs.get('essay_ids', [])
        user = attrs.get('user')
        if user is None:
            raise serializers.ValidationError("Se debe proporcionar la id del usuario.")
        for essay_id in essay_ids:
            try:
                essay = Essay.objects.get(id=essay_id)
            except Essay.DoesNotExist:
                raise serializers.ValidationError(f"La ID del ensayo {essay_id} no existe.")
        return attrs


    def create(self, validated_data):
        essay_ids = validated_data.pop('essay_ids', [])
        custom_essay = CustomEssay.objects.create(**validated_data)
        for essay_id in essay_ids:
            essay = Essay.objects.get(id=essay_id)
            EssayAnswer.objects.create(essay=essay, custom_essay=custom_essay)
        return custom_essay


class CustomEssayQuestionSerializer(serializers.ModelSerializer):
    questions = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Question.objects.filter(is_deleted=False)))

    class Meta:
        model = CustomEssayQuestion
        fields = ['custom_essay', 'questions']

    def validate(self, attrs):
        custom_essay = attrs.get('custom_essay')
        questions = attrs.get('questions')

        try:
            custom_essay_obj = CustomEssay.objects.get(id=custom_essay)
        except CustomEssay.DoesNotExist:
            raise serializers.ValidationError('El ensayo personalizado no existe.')
        # Verificar que las preguntas existan en los ensayos seleccionados
        essay_ids = custom_essay_obj.essays.values_list('id', flat=True)
        for question_id in questions:
            try:
                question_obj = Question.objects.get(id=question_id)
                if question_obj.essays.filter(id__in=essay_ids).exists():
                    continue
                else:
                    raise serializers.ValidationError('Una o más preguntas no existen en los ensayos predefinidos seleccionados del ensayo personalizado.')
            except Question.DoesNotExist:
                raise serializers.ValidationError('Una o más preguntas no existen en los ensayos predefinidos seleccionados del ensayo personalizado.')

        return attrs

