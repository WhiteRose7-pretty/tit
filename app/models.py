from ckeditor.fields import RichTextField
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit

from authentication.models import CustomUser
from . import const


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa kategorii')
    menu = models.BooleanField(default=False, verbose_name='Pokaż w menu')
    slug = models.SlugField(unique=True, max_length=500, null=True, blank=True)

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
                                      verbose_name='Zdjęcie (proferowany format 730x450)',
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
        return '%s - %s | Widoczny: %s' % (self.name, self.owner.title, self.display)


class AddCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(verbose_name='slug for Category', unique=True, max_length=500)
    img_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Add(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(AddCategory, verbose_name="Category", related_name='adds',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='slug', unique=True, max_length=500)
    background_img = ProcessedImageField(upload_to='add-pictures',
                                         verbose_name='background image',
                                         processors=[ResizeToFill(1920, 1080)],
                                         format='JPEG',
                                         options={'quality': 100}, blank=True, null=True)
    img_300x170 = ImageSpecField(source='background_img',
                               processors=[ResizeToFill(300, 170)],
                               format='JPEG',
                               options={'quality': 80})
    img_730x411 = ImageSpecField(source='background_img',
                                 processors=[ResizeToFill(730, 411)],
                                 format='JPEG',
                                 options={'quality': 80})

    content = models.TextField(verbose_name="Content", blank=True, null=True, default='')
    phone_number = models.CharField(blank=True, null=True, max_length=30)
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    words = models.IntegerField(default=0)
    time_of_broadcast = models.IntegerField(verbose_name='Time of broadcast(weeks)', default=1)
    price = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    def __str__(self):
        return self.content


class PrivacyPolicy(models.Model):
    privacy = RichTextField()
    regulations = RichTextField()

    class Meta:
        verbose_name = 'Polityka prywatności i regulamin'
        verbose_name_plural = 'Polityka prywatności i regulamin'


class SubscriberEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class AdsSetting(models.Model):
    word_limit = models.IntegerField(default=500)
    price_word = models.DecimalField(decimal_places=1, max_digits=2, default=1.0)
    price_image = models.DecimalField(decimal_places=1, max_digits=3, default=10.0)
    tax_rate = models.DecimalField(decimal_places=3, max_digits=4, default=0.074)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, null=True, )
    email = models.EmailField(max_length=100, null=True,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


CHOICE_TIME_UNIT = [
    ('week', 'week'),
    ('month', 'month'),
    ('year', 'year'),
]

CHOICE_ACCESS_TYPE = [
    ('full content', 'full content'),
    ('full text', 'full text')
]


class FullAccess(models.Model):
    time_string = models.CharField(max_length=50, default='month')
    unit = models.CharField(max_length=50, choices=CHOICE_TIME_UNIT)
    time = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    type = models.CharField(max_length=200, choices=CHOICE_ACCESS_TYPE)

    def __str__(self):
        return self.time_string


class FullAccessSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(FullAccess, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)


class Przelewy24Transaction(models.Model):
    """
        model for storing P24 transaction
    """
    p24_session_id = models.CharField(u"P24 session id", max_length=64)
    p24_id_sprzedawcy = models.CharField(u"Vendor Id", max_length=10)
    p24_email = models.EmailField(u'Vendor email')
    p24_kwota = models.CharField(u"Amount", max_length=10)
    p24_order_id = models.CharField(
        u"Order ID", max_length=100, null=True, blank=True)
    p24_order_id_full = models.CharField(
        u"Order ID Full", max_length=100, null=True, blank=True)

    p24_return_url_ok = models.URLField(u"Return URL OK")
    p24_return_url_error = models.URLField(u"Return URL ERROR")

    p24_karta = models.CharField(
        u"CC?", max_length=10, blank=True, null=True)
    p24_opis = models.TextField(u"Description", null=True, blank=True)

    p24_crc = models.CharField(
        u"CHECKSUM HASH", max_length=32,
        help_text=u'In our request to P24 - will be verified by P24')
    p24_crc2 = models.CharField(
        u"CHECKSUM HASH 2", max_length=32,
        help_text=u'In response from P24 - needs to be verified by us')

    p24_error_code = models.CharField(u"Error code", max_length=7, blank=True)
    p24_error_desc = models.CharField(u"Error description", max_length=255,
                                      null=True, blank=True)

    status = models.IntegerField(
        u"Transaction status",
        default=const.P24_STATUS_INITIATED,
        choices=const.P24_STATUS_CHOICES)

    created_at = models.DateTimeField(u"Created date", auto_now_add=True)
    updated_at = models.DateTimeField(u"Updated date", auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __unicode__(self):
        return u'%s' % self.p24_session_id