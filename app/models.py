from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa kategorii')
    menu = models.BooleanField(default=False, verbose_name='Pokaż w menu')

    class Meta:
        verbose_name = 'Kategorii artykułów'
        verbose_name_plural = 'Kategorii artykułów'

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoria artykułu')
    title = models.CharField(max_length=100, verbose_name='Tytuł artykułu')
    img = models.ImageField(verbose_name='Zdjęcie')
    date_of_publication = models.DateTimeField(verbose_name='Data publikacji')
    content = RichTextField(verbose_name='Treść artykułu')
    premium = models.BooleanField(default=True, verbose_name='Widoczne tylko dla PREMIUM')

    class Meta:
        verbose_name = 'Artykuły'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        return self.title