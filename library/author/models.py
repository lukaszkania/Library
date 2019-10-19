from django.db import models

# Create your models here.
class Author(models.Model):
    authorName = models.CharField(max_length=100, null=False, unique=True)
    booksWritten = models.ForeignKey("books.Book", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.authorName