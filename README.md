# Отчёт

## Django rest auth

Для подключения и настройки Django Rest Auth:

1. Установите Django Rest Auth через pip:

    ```
    pip install django-rest-auth
    ```

2. Добавьте `'rest_auth'` в INSTALLED_APPS в файле settings.py:

    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'rest_auth',  # Добавьте эту строку
        ...
    ]
    ```

3. Настройте URL маршруты в urls.py:

    ```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('api-auth/', include('rest_framework.urls')),
        path('rest-auth/', include('rest_auth.urls')),  # Добавьте эту строку
        path('rest-auth/registration/', include('rest_auth.registration.urls')),  # Добавьте эту строку, если нужна регистрация
        ...
    ]
    ```

4. Настройте аутентификацию в settings.py:

    ```python
    REST_FRAMEWORK = {
        ...
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',  # Добавьте эту строку
            'rest_framework.authentication.SessionAuthentication',
        ),
        ...
    }
    ```

Это позволит использовать TokenAuthentication для аутентификации пользователей через Django Rest Auth.

## DRF pagination

Для настройки пагинации в Django Rest Framework (DRF):

1. Определите пагинатор в settings.py:

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,  # Укажите желаемый размер страницы
    }
    ```

2. Добавьте пагинатор к представлениям, где это необходимо. Например:

    ```python
    from rest_framework.pagination import PageNumberPagination
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from .models import Post
    from .serializers import PostSerializer

    class PostList(APIView):
        def get(self, request):
            paginator = PageNumberPagination()
            paginator.page_size = 10  # Можно указать размер страницы здесь, если он отличается от PAGE_SIZE в settings.py
            posts = Post.objects.all()
            result_page = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
    ```

Это позволит пагинировать результаты с учетом настроек, указанных в settings.py.

## Unit Test

Для написания unit-тестов в Django с использованием модуля `unittest`:

1. Создайте тестовый файл, например tests.py, и определите в нем ваши тесты.

2. Напишите тесты, используя методы TestCase, например:

    ```python
    import unittest

    def add(a, b):
        return a + b

    class TestAddFunction(unittest.TestCase):
        def test_add_positive_numbers(self):
            result = add(3, 5)
            self.assertEqual(result, 8)

        def test_add_negative_numbers(self):
            result = add(-3, -5)
            self.assertEqual(result, -8)

        def test_add_mixed_numbers(self):
            result = add(3, -5)
            self.assertEqual(result, -2)

    if __name__ == '__main__':
        unittest.main()
    ```

3. Запустите тесты, выполнив файл.

## Pytest

Для написания тестов с использованием pytest в Django:

1. Установите pytest и pytest-django через pip:

    ```
    pip install pytest pytest-django
    ```

2. Напишите ваши тесты, используя pytest, например:

    ```python
    # tests.py
    import pytest
    from django.urls import reverse
    from myapp.models import MyModel

    @pytest.mark.django_db
    def test_my_model_creation():
        MyModel.objects.create(name='Test')
        assert MyModel.objects.count() == 1

    @pytest.mark.django_db
    def test_my_view(client):
        response = client.get(reverse('my_view_name'))
        assert response.status_code == 200
        assert 'Welcome' in response.content.decode('utf-8')
    ```

3. Запустите тесты, выполните команду `pytest` в корневой директории вашего проекта.

## Asyncio

Для работы с асинхронным кодом в Python используйте модуль asyncio. Вот пример асинхронного приложения:

```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)  # имитируем задержку в 1 секунду
    print("Hello")

async def say_world():
    await asyncio.sleep(2)  # имитируем задержку в 2 секунды
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_world())

if __name__ == "__main__":
    asyncio.run(main())
```

## Celery

Для работы с Celery:

1. Установите Celery:

    ```
    pip install celery
    ```

2. Создайте файл tasks.py, где определите вашу фоновую задачу:

    ```python
    # tasks.py
    from celery import Celery

    app = Celery('tasks', broker='redis://localhost:6379/0')

    @app.task
    def add(x, y):
        return x + y
    ```

3. Запустите Celery worker:

    ```
    celery -A tasks worker --loglevel=info
    ```

4. Используйте задачу в вашем коде, например:

    ```python
    from tasks import add

    result = add.delay(4, 4)
    print(result.get())  # Получить результат
    ```

Это простой пример использования Celery для асинхронного выполнения задачи сложения двух чисел. Помимо этого, Celery поддерживает множество расширенных функций, таких как периодические задачи, очереди задач и многое другое.
