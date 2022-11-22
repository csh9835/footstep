from django.shortcuts import render
from .models import Post, User

def index(request):
    test = Post.objects.order_by('-create_date')
    context = {'test':test}
    return render(request, 'footstep/main.html', context)

def personal(request, username):
    user = User.objects.get(username=username)
    personal = user.post_set.all()
    context = {'personal': personal}
    return render(request, 'footstep/personal.html', context)