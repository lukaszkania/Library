from django.urls import path, include
from books.views import AllBooksView

urlpatterns = [
    path("", AllBooksView.as_view(), name="books-list")
]