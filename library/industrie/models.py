from django.db import models

# Create your models here.
class Industrie(models.Model):
    type_of_industrie = models.CharField(max_length=10, null=False)
    identifier = models.CharField(max_length=100, null=False)
    released_books = models.ForeignKey("books.Book", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        industrie = {
            "type_of_industrie": self.type_of_industrie,
            "identifier": self.identifier
        }
        return str(industrie)[1:-1]