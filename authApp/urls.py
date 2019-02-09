from django.conf.urls import url
from django.urls import path, include, reverse
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'auth'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:person_id>/', views.detail, name='profile'),
    path('login/', LoginView.as_view(template_name=r'auth\registration\login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name=r'auth\registration\login.html'), name='logout'),
    path('create/', views.create_user_view, name='create'),
    path('users/', views.user_formset_view, name='users'),
]
