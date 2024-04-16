from rest_framework import generics
from .models import Author, Genre, Book, Borrow
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, BorrowSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowListCreate(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get(self, request, *args, **kwargs):
        # Получаем id книги из запроса
        book_id = request.query_params.get('book_id')

        if book_id:
            try:
                borrow = Borrow.objects.get(book__id=book_id)
                # Сериализуем данные
                serializer = self.serializer_class(borrow, context={'request': request})

                # Возвращаем список бронирований данного пользователя
                return Response(serializer.data)
            except:
                return []
        
        # Получаем id пользователя из запроса
        borrower_id = request.query_params.get('borrower_id')
        if borrower_id:
            # Фильтруем бронирования по id пользователя
            borrows = Borrow.objects.filter(borrower_id=borrower_id)

            # Сериализуем данные
            serializer = self.serializer_class(borrows, context={'request': request}, many=True)

            # Возвращаем список бронирований данного пользователя
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Получаем данные из запроса
        book_id = request.data.get('book_id')
        borrower_id = request.data.get('borrower_id')

        print(book_id, borrower_id)

        # Получаем экземпляр книги или возвращаем 404, если книга не найдена
        book = get_object_or_404(Book, pk=book_id)

        # Создаем бронирование
        borrow = Borrow.objects.create(book=book, borrower_id=borrower_id)

        # Сериализуем созданное бронирование
        serializer = BorrowSerializer(borrow)

        # Возвращаем успешный ответ
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BorrowRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

