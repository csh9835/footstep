from django.shortcuts import render, get_object_or_404
from .models import Post, User

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