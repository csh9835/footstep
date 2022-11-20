from django.urls import path

from . import views

app_name = 'footstep'

urlpatterns = [
    path('', views.index, name='index'),
    path('personal/', views.personal, name='personal'),
]