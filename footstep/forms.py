from django import forms
from .models import Comment

class PostForm(forms.Form):
    subject = forms.CharField(max_length=200)
    category = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    labels = {
        'subject': '제목',
        'category': '카테고리',
        'content': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }
