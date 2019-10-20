from django.urls import path, include
from books.views import AllBooksView, AddNewBookView

urlpatterns = [
    path("", AllBooksView.as_view(), name="books-list"),
    path("add-new-book", AddNewBookView.as_view(), name="add-new-book"),
]