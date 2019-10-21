from django.db import models
from django.core.validators import MinValueValidator 
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    published_date = models.CharField(max_length=11, null=False)
    page_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    language = models.CharField(max_length=10, null=False)
    small_thumbnail = models.CharField(max_length=1000, null=True, default="Undefined")
    thumbnail = models.CharField(max_length=1000, null=True, default="Undefined")
    authors = models.ManyToManyField("author.Author")
    industries = models.ManyToManyField("industrie.Industrie")

    def get_absolute_url(self):
        return reverse('books-list')

    def __str__(self):
        return self.title