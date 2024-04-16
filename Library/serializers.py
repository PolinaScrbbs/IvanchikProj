from rest_framework import serializers
from .models import Author, Genre, Book, Borrow

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = AuthorSerializer()
    genre = GenreSerializer()
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            print(self.context['request'].build_absolute_uri(obj.cover_image.url))
            return self.context['request'].build_absolute_uri(obj.cover_image.url)
        return None    

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Borrow
        fields = '__all__'

