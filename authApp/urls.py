from django.conf.urls import url
from django.urls import path, include, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from authApp.views import IndexView, DetailView, UsersView

app_name = 'auth'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('profile/<int:person_id>/', views.detail, name='profile'),
    path('login/', LoginView.as_view(
        template_name=r'authApp\registration\login.html', extra_context={
            'extended_template': settings.BASE_WITH_HEADER_TEMPLATE}),
         name='login'),
    path('logout/', LogoutView.as_view(
        template_name=r'authApp\registration\logout.html', extra_context={
            'extended_template': settings.BASE_WITH_HEADER_TEMPLATE}), name='logout'),
    path('detail/', DetailView.as_view(), name='detail'),
    # path('create/', views.create_user_view, name='create'),
    path('users/', UsersView.as_view(), name='users'),
]
