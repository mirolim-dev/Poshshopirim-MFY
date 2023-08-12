from django.urls import path

from .views import home
from news.views import post

urlpatterns = [
    path('', post, name='home'),
]
