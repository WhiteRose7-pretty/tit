from django import forms
from .models import HomePage
from django.forms import DateTimeInput
from app.models import Article
from django.forms import FileInput



class NewPostForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Podaj nazwę...'}))
    date = forms.DateTimeField(widget=DateTimeInput(attrs={'class': 'form-control form-control',
                                                           'data-mask': '0000-00-00 00:00:00',
                                                           'placeholder': '2020-01-01 00:00:00'}))



class FindArticleForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Article.objects.all(),
                                  empty_label='Wybierz artykuł...',
                                  required=False,
                                  widget=forms.Select(attrs={'data-toggle': 'select',
                                                             'class': 'form-control'}))



class UploadImageForm(forms.Form):
    img = forms.ImageField(widget=FileInput(attrs={'class': 'custom-input-file','accept': '.jpg, .jpeg',}))



class ChangeLabelOnPage(forms.Form):
    button_1 = forms.CharField(max_length=11, label='Przycisk 1', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Przycisk 1'}))
    button_2 = forms.CharField(max_length=11, label='Przycisk 2', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Przycisk 2'}))
    button_3 = forms.CharField(max_length=11, label='Przycisk 3', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Przycisk 3'}))
    section_1 = forms.CharField(max_length=50, label='Sekca 1', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 1'}))
    section_2 = forms.CharField(max_length=50, label='Sekca 2', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 2'}))
    section_3 = forms.CharField(max_length=50, label='Sekca 3', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 3'}))
    section_4 = forms.CharField(max_length=50, label='Sekca 4', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 4'}))
    section_5 = forms.CharField(max_length=50, label='Sekca 5', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 5'}))
    section_6 = forms.CharField(max_length=50, label='Sekca 6', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 6'}))
    section_7 = forms.CharField(max_length=50, label='Sekca 7', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 7'}))
    section_8 = forms.CharField(max_length=50, label='Sekca 8', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Sekcja 8'}))