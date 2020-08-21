from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from authentication.models import CustomUser
import datetime



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa kategorii')
    menu = models.BooleanField(default=False, verbose_name='Pokaż w menu')

    class Meta:
        verbose_name = 'Kategorie artykułów'
        verbose_name_plural = 'Kategorie artykułów'

    def __str__(self):
        return self.name



class Autor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Imię i nazwisko')
    pseudonym = models.CharField(max_length=50, verbose_name='Pseudonim')
    img = ProcessedImageField(upload_to='profile-pictures',
                              processors=[ResizeToFill(400, 400)],
                              format='JPEG',
                              options={'quality': 100},
                              verbose_name='Zdjęcie (proferowany format 730x450)')
    description = models.TextField(null=True, verbose_name='Opis (opcjonalnie)')

    class Meta:
        verbose_name = 'Autorzy'
        verbose_name_plural = 'Autorzy'

    def __str__(self):
        return self.name



class Article(models.Model):
    owner = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoria artykułu')
    title = models.CharField(max_length=100, verbose_name='Tytuł artykułu')
    subtitle = models.TextField(verbose_name='Rozszerzenie tytulu artykulu')
    slug = models.SlugField(verbose_name="URL artykułu (zmieniać w ramach konieczności):", unique=True)
    img = ProcessedImageField(upload_to='profile-pictures',
                              processors=[ResizeToFill(730, 450)],
                              format='JPEG',
                              options={'quality': 100},
                              verbose_name='Zdjęcie (proferowany format 730x450)')
    date_of_publication = models.DateTimeField(verbose_name='Data publikacji')
    content = RichTextField(verbose_name='Treść artykułu')
    premium = models.BooleanField(default=True, verbose_name='Widoczne tylko dla PREMIUM')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Artykuły'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        return self.title



class Comment(models.Model):
    owner = models.ForeignKey(Article,
                              on_delete=models.CASCADE,
                              related_name='comments',
                              verbose_name='Artykuł')
    name = models.CharField(max_length=30, verbose_name='Imie lub pseudonim')
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             null=True,
                             verbose_name='Jeżeli dodawał zalogowany użytkownik')
    content = models.TextField(verbose_name='Treść dodawanej opinii')
    display = models.BooleanField(default=False, verbose_name='Widoczny komentarz')

    class Meta:
        verbose_name = 'Komentarze użytkowników'
        verbose_name_plural = 'Komentarze użytkowników'

    def __str__(self):
        return '%s - %s | Widoczny: %s'% (self.name, self.owner.title, self.display)

