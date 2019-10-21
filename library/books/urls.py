from django.urls import path, include
from books.views import AllBooksView, AddNewBookView, ImportBooksFromAPIView

urlpatterns = [
    path("", AllBooksView.as_view(), name="books-list"),
    path("add-new-book", AddNewBookView.as_view(), name="add-new-book"),
    path("import-books-from-api/", ImportBooksFromAPIView.as_view(), name="import-books-from-api"),
]