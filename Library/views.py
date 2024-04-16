from django.shortcuts import render, redirect
import requests
import openpyxl

from .forms import ExcelUploadForm

def index(request):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    # Выполняем GET-запрос к вашему API для получения списка книг
    api_url = 'http://127.0.0.1:8000/api/books/'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Если запрос успешен, получаем данные о преподавателях из ответа API
        books = response.json()

        # Передаем данные о преподавателях в контекст представления
        context = {
            'user': user,
            'title': 'Рассписание',
            'books': books
        }
        return render(request, 'index.html', context)
    else:
        # Если запрос не удался, возвращаем пустой список преподавателей
        books = []
        context = {
            'user': user,
            'title': 'Рассписание',
            'books': books
        }
        return render(request, 'index.html', context)

def book_info(request, book_id):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    # Выполняем GET-запрос к вашему API для получения информации о книге
    book_api_url = f'http://127.0.0.1:8000/api/books/{book_id}/'
    book_response = requests.get(book_api_url)

    # Выполняем GET-запрос к вашему API для получения информации о бронировании книги
    borrow_api_url = f'http://127.0.0.1:8000/api/borrows/?book_id={book_id}'
    borrow_response = requests.get(borrow_api_url)

    if book_response.status_code == 200:
        # Если запрос успешен, получаем данные о книге из ответа API
        book = book_response.json()

        # Если запрос о бронировании также успешен, получаем данные о бронировании
        if borrow_response.status_code == 200:
            borrow = borrow_response.json()
        else:
            borrow = None

        # Передаем данные о книге и бронировании в контекст представления
        context = {
            'user': user,
            'title': book['title'],
            'book': book,
            'borrow': borrow
        }
        return render(request, 'book_info.html', context)
    else:
        # Если запрос не удался, возвращаем пустые данные о книге и бронировании
        book = {}
        borrow = None
        context = {
            'user': user,
            'title': 'Ошибка',
            'book': book,
            'borrow': borrow
        }
        return render(request, 'book_info.html', context)

def borrows(request):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    if user:
        # Получаем список бронирований для данного пользователя
        borrows_url = f'http://127.0.0.1:8000/api/borrows/?borrower_id={user['id']}'
        borrows_response = requests.get(borrows_url)
            
        if borrows_response.status_code == 200:
            borrows = borrows_response.json()
            static = {
                'user': user,
                'title': f'Брони {user['full_name']}',
                'borrows': borrows
            }

            return render(request, 'borrows.html', static)

        else:
            # Если запрос о бронированиях не удался, возвращаем пустой список
            return []
    else:
        # Если запрос о пользователе не удался, возвращаем пустой список
        return []


def borrow_book(request, book_id):
    token = request.session.get('token')
    if token:
        api_url = f'http://127.0.0.1:8000/auth/signup/?token={token}'
        response = requests.get(api_url)

        if response.status_code == 200:
            user = response.json()['Пользователь']
        else:
            print("Ошибка:", response.status_code)
    else:
        user = None

    if user:
        # Подготавливаем данные для запроса
        data = {
            'book_id': book_id,
            'borrower_id': user['id']
        }

        # Выполняем POST-запрос к вашему API для создания бронирования
        api_url = 'http://127.0.0.1:8000/api/borrows/'
        response = requests.post(api_url, data=data)

        # Проверяем, успешен ли запрос
        if response.status_code == 201:
            # Если бронирование успешно создано, перенаправляем пользователя на страницу с информацией о книге
            return redirect('book_info', book_id=book_id)
        else:
            # Если запрос не удался, перенаправляем пользователя на страницу с сообщением об ошибке
            return render(request, 'error.html', {'message': 'Ошибка при бронировании книги'})
    else:
        return redirect('login')



