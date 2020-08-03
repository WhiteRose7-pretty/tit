from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.BooleanField(default=False)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img = models.ImageField()
    date_of_publication = models.DateTimeField()
    content = RichTextField()
    premium = models.BooleanField(default=True)