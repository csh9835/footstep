from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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

def post_create(request, username):
    owner = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
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
    return render(request, 'footstep/post_create.html', context)