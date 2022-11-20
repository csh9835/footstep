from django.shortcuts import render
from .models import Post

def index(request):
    test = Post.objects.order_by('-create_date')
    context = {'test':test}
    return render(request, 'footstep/main.html', context)

def personal(request):
    return render(request, 'footstep/personal.html')