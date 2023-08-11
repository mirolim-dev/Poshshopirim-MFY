from django.urls import path

from .views import post, posts_by_category, post_detail

urlpatterns = [
    path('', post, name='post'), 
    path('<str:tag>/', posts_by_category, name='posts_by_category'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
]
