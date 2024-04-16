from django.urls import path
from .views import index, book_info, borrows, borrow_book

urlpatterns = [
    path('', index, name='index'),
    path('book/<int:book_id>', book_info, name='book_info'),
    path('borrows', borrows, name='borrows'),
    path('borrow_book/<int:book_id>', borrow_book, name='borrow_book'),
]