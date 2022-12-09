from django.urls import path

from . import views

app_name = 'footstep'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.personal, name='personal'),
    path('<str:username>/category=<str:category_sub>/', views.category, name='category'),
    path('<str:username>/category=<str:category_sub>/delete/', views.category_delete, name='category_delete'),    
    path('<str:username>/post=<str:subject>/', views.post, name='post'),
    path('<str:username>/create/', views.post_create, name='post_create'),
    path('<str:username>/post=<str:subject>/modify/', views.post_modify, name='post_modify'),
    path('<str:username>/post=<str:subject>/delete/', views.post_delete, name='post_delete'),
    path('<str:username>/post=<str:subject>/comment_create/', views.comment_create, name='comment_create'),
    path('<str:username>/post=<str:subject>/comment_modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('<str:username>/post=<str:subject>/comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]