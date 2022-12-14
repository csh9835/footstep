from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/modify/', views.profile_modify, name='profile_modify'),
    path('profile/password_change/', views.password_change, name='password_change'),
    path('delete/', views.profile_delete, name='profile_delete')
]