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