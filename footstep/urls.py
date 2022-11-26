from django.urls import path

from . import views

app_name = 'footstep'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.personal, name='personal'),
    path('<str:username>/<str:category_sub>/', views.category, name='category'),
]