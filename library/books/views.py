from django.shortcuts import render
from django.views.generic.list import ListView
from books.models import Book
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.db.models import Q 
from author.models import Author

# Create your views here.
class AllBooksView(ListView):
    model = Book
    template_name = "booksList.html"
    context_object_name = "booksList"
    
    def get_queryset(self):
        searchedPhrase = self.request.GET.get('question')
        if(searchedPhrase):
            return Book.objects.filter(
            Q(title__icontains=searchedPhrase) |
            Q(language__icontains=searchedPhrase) | 
            Q(published_date__icontains=searchedPhrase) |
            Q(authors__authorName__icontains=searchedPhrase)
            ) 
        return Book.objects.all()
    
class AddNewBookView(CreateView):
    model = Book
    template_name = "addBook.html"
    fields = ["title", "published_date", "page_count", "language", "small_thumbnail", "thumbnail", "authors", "industries"]


