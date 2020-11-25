from django import forms
from .models import Add, SubscriberEmail


class NewAddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ('category', 'content', 'slug', 'background_img', 'time_of_broadcast',)
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control px-1  mb-4'}),
            'slug': forms.TextInput(attrs={'class': 'form-control px-1  mb-4'}),
            'background_img': forms.FileInput(attrs={'class': 'custom-file-input', 'accept': "image/*"}),
            'content': forms.Textarea(attrs={'class': 'form-control px-1  mb-4', 'rows': "3"}),
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscriberEmail
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': "signup", 'placeholder': "Twój adres email"})
        }

