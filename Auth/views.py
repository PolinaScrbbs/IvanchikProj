from django.contrib.auth import authenticate

from .models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .functions import get_user_by_token

#Получение и добавление пользователей
class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        serializer = self.get_serializer(user)
        return Response({"Пользователь": serializer.data})

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Создан пользователь": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Авторизация и создание токена
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ошибка аутентификации'}, status=status.HTTP_401_UNAUTHORIZED)
