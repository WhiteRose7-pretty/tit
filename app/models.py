from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from authentication.models import CustomUser
import datetime
from imagekit.processors import ResizeToFit



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
                              verbose_name='Zdjęcie (proferowany format 400x400)')
    description = models.TextField(null=True, verbose_name='Opis (opcjonalnie)')
    show_img = models.BooleanField(default=False, verbose_name='Pokaż zdjęcie użytkownika')

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
    img_classic = ProcessedImageField(upload_to='profile-pictures',
                                      verbose_name = 'Zdjęcie (proferowany format 730x450)',
                                      processors=[ResizeToFit(1920, 1920)],
                                      format='JPEG',
                                      options={'quality': 100})
    img = ImageSpecField(source='img_classic',
                              processors=[ResizeToFill(730, 450)],
                              format='JPEG',
                              options={'quality': 100})
    basic_img = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(1460, 1000)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_95x70 = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(95, 70)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_190x140 = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(190, 140)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_200x154 = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(200, 154)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_728x90 = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(728, 90)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_700x500 = ImageSpecField(source='img_classic',
                                      processors=[ResizeToFill(700, 500)],
                                      format='JPEG',
                                      options={'quality': 80})
    img_360x115 = ImageSpecField(source='img_classic',
                                 processors=[ResizeToFill(360, 115)],
                                 format='JPEG',
                                 options={'quality': 80})
    img_160x128 = ImageSpecField(source='img_classic',
                                 processors=[ResizeToFill(160, 128)],
                                 format='JPEG',
                                 options={'quality': 80})
    img_1080x840 = ImageSpecField(source='img_classic',
                                  processors=[ResizeToFill(1080, 840)],
                                  format='JPEG',
                                  options={'quality': 80})
    img_1460x822 = ImageSpecField(source='img_classic',
                                  processors=[ResizeToFill(1460, 822)],
                                  format='JPEG',
                                  options={'quality': 80})
    img_200x113 = ImageSpecField(source='img_classic',
                                 processors=[ResizeToFill(200, 113)],
                                 format='JPEG',
                                 options={'quality': 80})
    img_540x640 = ImageSpecField(source='img_classic',
                                 processors=[ResizeToFill(540, 640)],
                                 format='JPEG',
                                 options={'quality': 80})

    date_of_publication = models.DateTimeField(verbose_name='Data publikacji')
    content = RichTextField(verbose_name='Treść artykułu')
    premium = models.BooleanField(default=True, verbose_name='Widoczne tylko dla PREMIUM')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    add = models.BooleanField(default=False, verbose_name='Czy artykuł jest reklamą?')
    url = models.URLField(blank=True, null=True, verbose_name='Adres URL reklamy')

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
                             blank=True,
                             null=True,
                             verbose_name='Jeżeli dodawał zalogowany użytkownik')
    content = models.TextField(verbose_name='Treść dodawanej opinii')
    display = models.BooleanField(default=False, verbose_name='Widoczny komentarz')

    class Meta:
        verbose_name = 'Komentarze użytkowników'
        verbose_name_plural = 'Komentarze użytkowników'

    def __str__(self):
        return '%s - %s | Widoczny: %s'% (self.name, self.owner.title, self.display)


class Add(models.Model):
    name = models.CharField(max_length=100)


class PrivacyPolicy(models.Model):
    privacy = RichTextField()
    regulations = RichTextField()

    class Meta:
        verbose_name = 'Polityka prywatności i regulamin'
        verbose_name_plural = 'Polityka prywatności i regulamin'
