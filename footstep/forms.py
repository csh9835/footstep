from django import forms
from .models import Post

class PostForm(forms.Form):
    subject = forms.CharField(max_length=200)
    category = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)