from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'full_name']

        # Дополнительные параметры
        extra_kwargs = {
            'password': {'write_only': True},  #Пароль только для чтения
        }

    #Хеширование пароля
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = super(UserSerializer, self).create(validated_data)
        Token.objects.create(user=user)
        return user