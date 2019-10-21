from rest_framework import serializers
from books.models import Book
from author.models import Author
from industrie.models import Industrie

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("pk", "authorName")

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorsSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = ("title", "authors", "language", "published_date")

