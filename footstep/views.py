from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import User, Post, Comment
from .forms import PostForm, CommentForm


def search(obj, k):
    filter_obj = obj.filter(
        Q(subject__icontains=k) | #제목
        Q(content__icontains=k) | #내용
        Q(category__category_sub__icontains=k) | #카테고리
        Q(author__username__icontains=k) #작성자
    ).distinct()
    return filter_obj


def index(request):
    allposts = Post.objects.order_by('-create_date')
    kw = request.GET.get('kw', '')
    page = request.GET.get('page', '1')
    if kw:
        allposts = allposts.filter(
            Q(subject__icontains=kw) | #제목
            Q(content__icontains=kw) | #내용
            Q(category__category_sub__icontains=kw) | #카테고리
            Q(author__username__icontains=kw) #작성자
        ).distinct()
    paginator = Paginator(allposts, 10)
    pagination = paginator.get_page(page)
    context = {'allposts':pagination, 'pagination':pagination, 'page': page, 'kw': kw}
    return render(request, 'footstep/main.html', context)


def personal(request, username):
    owner = get_object_or_404(User, username=username)
    posts = owner.author_post.order_by('-create_date')
    kw = request.GET.get('kw', '')
    if kw:
        posts = posts.filter(
            Q(subject__icontains=kw) | #제목
            Q(content__icontains=kw) | #내용
            Q(category__category_sub__icontains=kw) #카테고리
        ).distinct()
    page = request.GET.get('page', '1')
    paginator = Paginator(posts, 10)
    pagination = paginator.get_page(page)
    context = {'owner':owner, 'posts':pagination, 'pagination':pagination}
    return render(request, 'footstep/personal.html', context)


def category(request, username, category_sub):
    owner = get_object_or_404(User, username=username)
    category = get_object_or_404(owner.sidebarcontent_set, category_sub=category_sub)
    posts = category.post_set.order_by('-create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(posts, 10)
    pagination = paginator.get_page(page)
    context = {'owner':owner, 'category':category, 'posts':pagination, 'pagination':pagination}
    return render(request, 'footstep/category.html', context)


@login_required(login_url='common:login')
def category_delete(request, username, category_sub):
    owner = get_object_or_404(User, username=username)
    category = get_object_or_404(owner.sidebarcontent_set, category_sub=category_sub)
    if request.user != category.owner: #비정상 루트로 수행시
        messages.error(request, '삭제권한이 없습니다')
    else:
        category.delete()
    return redirect('footstep:personal', username=username)


def post(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.author_post, subject=subject)
    comments = post.comment_set.order_by('create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 10)
    pagination = paginator.get_page(page)
    context = {'owner':owner, 'post':post, 'comments':pagination, 'pagination':pagination}
    return render(request, 'footstep/post.html', context)


@login_required(login_url='common:login')
def post_create(request, username):
    owner = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            if post.subject != form.cleaned_data['subject'] and owner.author_post.filter(subject=form.cleaned_data['subject']): #게시글 제목 중복방지
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
    post = get_object_or_404(owner.author_post, subject=subject)
    i = {'subject':post.subject, 'category':post.category, 'content':post.content}
    if request.user != post.author: #비정상 루트로 수행시
        messages.error(request, '수정권한이 없습니다')
        return redirect('footstep:personal', username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if post.subject != form.cleaned_data['subject'] and owner.author_post.filter(subject=form.cleaned_data['subject']): #게시글 제목 중복방지
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
    post = get_object_or_404(owner.author_post, subject=subject)
    if request.user != post.author: #비정상 루트로 수행시
        messages.error(request, '삭제권한이 없습니다')
        return redirect('footstep:personal', username=username)
    post.delete()
    return redirect('footstep:personal', username=username)


@login_required(login_url='common:login')
def comment_create(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.author_post, subject=subject)
    comments = post.comment_set.order_by('create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 10)
    pagination = paginator.get_page(page)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('footstep:post', username=username, subject=subject)
    else:
        form = CommentForm()
    context = {'owner':owner, 'post':post, 'form':form, 'comments':pagination, 'pagination':pagination}
    return render(request, 'footstep/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify(request, username, subject, comment_id):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.author_post, subject=subject)
    comments = post.comment_set.order_by('create_date')
    comment = get_object_or_404(comments, pk=comment_id)
    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 10)
    pagination = paginator.get_page(page)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('footstep:post', username=username, subject=subject)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('footstep:post', username=username, subject=subject)
    else:
        form = CommentForm(instance=comment)
    context = {'owner':owner, 'post':post, 'form':form, 'comments':pagination, 'pagination':pagination}
    return render(request, 'footstep/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete(request, username, subject, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author: #비정상 루트로 수행시
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('footstep:post', username=username, subject=subject)


@login_required(login_url='common:login')
def post_recommend(request, username, subject):
    owner = get_object_or_404(User, username=username)
    post = get_object_or_404(owner.author_post, subject=subject)
    if request.user == post.author:
        messages.error(request, '본인의 게시글은 추천할수 없습니다')
    else:
        post.recommend.add(request.user)
    return redirect('footstep:post', username=username, subject=subject)


@login_required(login_url='common:login')
def comment_recommend(request, username, subject, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인의 댓글은 추천할수 없습니다')
    else:
        comment.recommend.add(request.user)
    return redirect('footstep:post', username=username, subject=subject)