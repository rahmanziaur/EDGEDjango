from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='App_login/login.html'), name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
