from django import forms
from .models import Language, Word


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        labels = {
            'name': 'Язык'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['language', 'original', 'translation']
        labels = {
            'language': 'Язык',
            'original': 'Слово',
            'translation': 'Перевод'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
