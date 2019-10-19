from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    published_date = models.CharField(max_length=11, null=False)
    page_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    language = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.title