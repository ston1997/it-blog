from django import forms
from .models import Category, News

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='название', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='текст', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    is_published = forms.BooleanField(label='публикация', initial=True)
    category = forms.ModelChoiceField(empty_label='выберите категорию', label='категория', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))