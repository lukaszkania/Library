from books.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            "title":["icontains"], 
            "authors":["icontains"],
            "published_date":["icontains"],
            "language":["icontains"]
            }

class BookViewSet(viewsets.ViewSet):
    filterset_class = BookFilter
    model = BookSerializer.Meta.model
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


