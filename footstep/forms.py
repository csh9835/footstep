from django import forms
from .models import Comment

class PostForm(forms.Form):
    subject = forms.CharField(max_length=200, label='제목')
    category = forms.CharField(max_length=200, label='카테고리')
    content = forms.CharField(widget=forms.Textarea, label='내용')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }
