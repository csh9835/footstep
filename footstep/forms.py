from django import forms
from .models import Comment

class PostForm(forms.Form):
    subject = forms.CharField(max_length=200)
    category = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']