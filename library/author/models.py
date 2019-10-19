from django.db import models

# Create your models here.
class Author(models.Model):
    authorName = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.authorName