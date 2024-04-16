from django.urls import path


from .views import (
    AuthorListCreate, AuthorRetrieveUpdateDestroy,
    GenreListCreate, GenreRetrieveUpdateDestroy,
    BookListCreate, BookRetrieveUpdateDestroy,
    BorrowListCreate, BorrowRetrieveUpdateDestroy,
)

urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-retrieve-update-destroy'),
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('borrows/', BorrowListCreate.as_view(), name='borrow-list-create'),
    path('borrow/<int:pk>/', BorrowRetrieveUpdateDestroy.as_view(), name='borrow-retrieve-update-destroy'),
]
