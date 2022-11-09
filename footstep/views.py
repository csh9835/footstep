from django.shortcuts import render

def index(request):
    return render(request, 'footstep/main.html')