from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Profile

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        labels = {
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
        }

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'ID',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'blogname')
        labels = {
            'nickname': '닉네임',
            'blogname': '블로그 이름',
        }