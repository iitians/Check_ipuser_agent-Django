from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import ListDisplay

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='mainweb/login.html'), name='login'),
    path('home/', ListDisplay.as_view() , name='home'),
]
