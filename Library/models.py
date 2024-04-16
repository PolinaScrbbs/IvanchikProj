from django.db import models
from Auth.models import User

class Author(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    biography = models.TextField(blank=True, verbose_name='Краткая биография')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Жанр')
    publication_date = models.DateField(verbose_name='Дата публикации')
    summary = models.TextField(blank=True, verbose_name='Резюме')
    cover_image = models.ImageField(upload_to='covers/', blank=True, verbose_name='Обложка')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заёмщик')
    borrowed_date = models.DateField(auto_now_add=True, verbose_name='Дата взятия')
    return_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')
    returned = models.BooleanField(default=False, verbose_name='Возвращена')

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'

    def __str__(self):
        return f"{self.book.title} - {self.borrower.full_name}"

