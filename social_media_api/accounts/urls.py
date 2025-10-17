from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='accounts'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]