from django.urls import path

from .views import home, workers_view
from news.views import post

urlpatterns = [
    path('', post, name='home'),
    path('workers/', workers_view, name='workers_view'),
]
