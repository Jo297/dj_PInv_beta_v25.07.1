# inventory/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name='home'),
        path('home/', views.home, name='home'),
        path('add/', views.add_item, name='add_item'),
        path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
        path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
        path('register/', views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]























