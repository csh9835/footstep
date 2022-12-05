from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, User, SidebarContent
from .forms import PostForm


def index(request):
    allposts = Post.objects.order_by('-create_date')
    context = {'allposts':allposts}
    return render(request, 'footstep/main.html', context)


def personal(request, username):
    owner = get_object_or_404(User, username=username)
    posts = owner.post_set.order_by('-create_date')
    context = {'owner':owner, 'posts':posts}
    return render(request, 'footstep/personal.html', context)


def category(request, username, category_sub):
    owner = get_object_or_404(User, username=username)
    category = get_object_or_404(owner.sidebarcontent_set, category_sub=category_sub)
    context = {'owner':owner, 'category':category}
    return render(request, 'footstep/category.html', context)


def post(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.post_set, subject=subject)
    context = {'owner':owner, 'post':post}
    return render(request, 'footstep/post.html', context)


@login_required(login_url='common:login')
def post_create(request, username):
    owner = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            if post.subject != form.cleaned_data['subject'] and owner.post_set.filter(subject=form.cleaned_data['subject']): #게시글 제목 중복방지
                messages.error(request, '동일한 제목의 게시글이 있습니다')
            else:
                post.subject = form.cleaned_data['subject']
                post.content = form.cleaned_data['content']
                post.author = owner
                try: #기존 카테고리 이름이 있으면
                    post.category = owner.sidebarcontent_set.get(category_sub=form.cleaned_data['category'])
                except: #없다면 생성
                    post.category = owner.sidebarcontent_set.create(category_sub=form.cleaned_data['category'])
                post.create_date = timezone.now()
                post.save()
                return redirect('footstep:personal', username = username)
    else:
        form = PostForm()
    context = {'owner':owner, 'form':form}
    return render(request, 'footstep/post_form.html', context)


@login_required(login_url='common:login')
def post_modify(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.post_set, subject=subject)
    i = {'subject':post.subject, 'category':post.category, 'content':post.content}
    if request.user != post.author: #비정상 루트로 수행시
        messages.error(request, '수정권한이 없습니다')
        return redirect('footstep:personal', username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if post.subject != form.cleaned_data['subject'] and owner.post_set.filter(subject=form.cleaned_data['subject']): #게시글 제목 중복방지
                messages.error(request, '동일한 제목의 게시글이 있습니다')
            else:
                post.subject = form.cleaned_data['subject']
                post.content = form.cleaned_data['content']
                post.author = owner
                try: #기존 카테고리 이름이 있으면
                    post.category = owner.sidebarcontent_set.get(category_sub=form.cleaned_data['category'])
                except: #없다면 생성
                    post.category = owner.sidebarcontent_set.create(category_sub=form.cleaned_data['category'])
                post.modify_date = timezone.now()
                post.save()
                return redirect('footstep:personal', username=username)
    else: 
        form = PostForm(i)
    context = {'owner':owner, 'form':form}
    return render(request, 'footstep/post_form.html', context)


@login_required(login_url='common:login')
def post_delete(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.post_set, subject=subject)
    if request.user != post.author: #비정상 루트로 수행시
        messages.error(request, '삭제권한이 없습니다')
        return redirect('footstep:personal', username=username)
    post.delete()
    return redirect('footstep:personal', username=username)