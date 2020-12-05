from django import forms
from .models import Add, SubscriberEmail, ContactMessage, Przelewy24Transaction


class NewAddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ('category', 'content', 'phone_number', 'slug', 'featured', 'background_img', 'time_of_broadcast',)
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control px-1  mb-4'}),
            'slug': forms.TextInput(attrs={'class': 'form-control px-1  mb-4'}),
            'background_img': forms.FileInput(attrs={'class': 'custom-file-input', 'accept': "image/*"}),
            'content': forms.Textarea(attrs={'class': 'form-control px-1  mb-4', 'rows': "3"}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control px-1  mb-4'}),
            'featured': forms.CheckboxInput(attrs={'class': ' px-2  mb-4 ml-3'}),
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscriberEmail
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': "signup", 'placeholder': "Twój adres email"})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'content',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control px-1 mb-4'}),
            'email': forms.EmailInput(attrs={'class': 'form-control px-1 mb-4'}),
            'content': forms.Textarea(attrs={'class': 'form-control px-1 mb-4', 'rows': 3}),
        }


class Przelewy24PrepareForm(forms.Form):
    p24_session_id = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_id_sprzedawcy = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_email = forms.CharField(max_length=100, label='email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_kwota = forms.CharField(max_length=100, label='', widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    p24_opis = forms.CharField(max_length=100, label='title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_klient = forms.CharField(max_length=100, label='surname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_adres = forms.CharField(max_length=100, label='address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_kod = forms.CharField(max_length=100, label='zip code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_miasto = forms.CharField(max_length=100, label='city', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p24_kraj = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_language = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_return_url_ok = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_return_url_error = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    p24_crc = forms.CharField(max_length=100, label='', widget=forms.HiddenInput())
    telephone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    business = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tax_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
