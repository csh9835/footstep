from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm,CustomUserChangeForm ,ProfileForm, User
from .models import Profile
import os


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('footstep:index')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'common/signup.html', context)


@login_required(login_url='common:login')
def profile(request):
    user = request.user
    posts_create = user.author_post.order_by('-create_date')[:5]
    comments_create = user.author_comment.order_by('-create_date')[:7]
    context = {'posts_create':posts_create, 'comments_create':comments_create}
    return render(request, 'common/profile.html', context)


@login_required(login_url='common:login')
def profile_modify(request):
    user = get_object_or_404(User, username=request.user.username)
    p = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            before_img = user.profile.profile_img
        except:
            before_img = None
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if p:
            pform = ProfileForm(request.POST, request.FILES, instance=user.profile)
        else:
            pform = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and pform.is_valid():
            form.save()
            pro = pform.save(commit=False)
            if 'cb' in request.POST:
                os.remove(pro.profile_img.path)
                pro.profile_img.delete()
            elif before_img and before_img != pro.profile_img:
                os.remove(before_img.path)
            pro.user = request.user
            pro.save()
            return redirect('common:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        if p:
            pform = ProfileForm(instance=user.profile)
        else:
            pform = ProfileForm()
    context = {'form':form, 'pform':pform}
    return render(request, 'common/profile_modify.html', context)


@login_required(login_url='common:login')
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('common:profile')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'common/password_change.html', context)


@login_required(login_url='common:login')
def profile_delete(request):
    if request.POST.get('delete') == '회원탈퇴':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            try:
                os.remove(user.profile.profile_img.path)
            except:
                pass
            user.delete()
            logout(request)
            return redirect('footstep:index')
    messages.error(request, '잘못된 요청입니다')
    return render(request, 'common/profile.html')