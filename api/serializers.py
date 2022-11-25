from api.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


generic_fields = ['created', 'updated', 'is_deleted']


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


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields, 'essay', 'question', 'users']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields, 'essay']


class EssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Essay
        exclude = [*generic_fields,'users']


class QuestionsAlternativeAllSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True, read_only= True)


class EssayQuestionsAlternativeAllSerializer(EssaySerializer):
    question = QuestionsAlternativeAllSerializer(many=True, read_only=True)


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


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'Contraseña actual': 'No coincide'})
        return value