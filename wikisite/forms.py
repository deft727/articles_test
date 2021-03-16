from django import forms
from .models import Article


class EditArticleForm(forms.ModelForm):
    
    class Meta:
        model=Article
        fields=[
            'title','text',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].initial = 'title'

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=[
            'title','text',
        ]

