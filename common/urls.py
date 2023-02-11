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
    path('delete/', views.profile_delete, name='profile_delete'),
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='common/password_reset.html', 
            email_template_name='common/password_reset_email.html',
            success_url='/common/password_reset_done/'
        ), 
        name="password_reset"
    ),
    path('password_reset_confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='common/password_reset_confirm.html',
            success_url='/common/password_reset_complete/'
        ), 
        name="password_reset_confirm"
    ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='common/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='common/password_reset_complete.html'), name="password_reset_complete"),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]