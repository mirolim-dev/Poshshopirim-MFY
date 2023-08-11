from django.shortcuts import render

from .models import Post, PostCategory
# Create your views here.

def post(request):
    categories = PostCategory.objects.all()
    posts = Post.objects.prefetch_related('author')
    context = {
        'categories': categories, 
        'posts': posts,
    }
    return render(request, 'blog.html', context)


def posts_by_category(request, tag):
    categories = PostCategory.objects.all()
    category = PostCategory.objects.get(name=tag)
    context = {
        'categories': categories, 
        'posts': Post.objects.filter(category=category).prefetch_related('author'),
    }
    return render(request, 'blog.html', context)


def post_detail(request, pk:int):
    context = {
        'post': Post.objects.get(id=pk),
    }
    return render(request, 'detail.html', context)
