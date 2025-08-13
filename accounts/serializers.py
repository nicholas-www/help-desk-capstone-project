from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    To display all users in the database
    """

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'is_agent', 'date_of_birth'
        ]


class RegisterSerializer(serializers.ModelSerializer):
    """For registering new users """

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'email', 'is_agent',
            'date_of_birth', 'password', 'password2'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
