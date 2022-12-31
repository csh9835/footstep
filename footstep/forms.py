from django import forms
from .models import Comment, SidebarContent
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.Form):
    subject = forms.CharField(max_length=150, label='제목')
    subtitle = forms.CharField(max_length=150, label='소제목', required=False)
    category = forms.CharField(max_length=150, label='카테고리')
    content = forms.CharField(
        widget=SummernoteWidget(),
        label='내용'
    )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = SidebarContent
        fields = ['category_sub']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }