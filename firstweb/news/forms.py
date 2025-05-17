from .models import  News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
     class Meta:
        model = News
        fields = ['title', 'anons', 'text',]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название радости"
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс радости"
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст"
            }),
        }
