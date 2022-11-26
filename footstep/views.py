from django.shortcuts import render, get_object_or_404
from .models import Post, User

def index(request):
    allposts = Post.objects.order_by('-create_date')
    context = {'allposts':allposts}
    return render(request, 'footstep/main.html', context)

def personal(request, username):
    owneruser = get_object_or_404(User, username=username)
    posts = owneruser.post_set.order_by('-create_date')
    context = {'owneruser':owneruser, 'posts':posts}
    return render(request, 'footstep/personal.html', context)

def category(request, username, category_sub):
    owneruser = get_object_or_404(User, username=username)
    category = get_object_or_404(owneruser.sidebarcontent_set, category_sub=category_sub)
    context = {'owneruser':owneruser, 'category':category}
    return render(request, 'footstep/category.html', context)