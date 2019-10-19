from django.shortcuts import render
from django.views.generic.list import ListView
from books.models import Book

# Create your views here.
class AllBooksView(ListView):
    model = Book
    paginate_by = 10
    template_name = "booksList.html"
    context_object_name = "booksList"

    def get_queryset(self):
        return Book.objects.all()
    