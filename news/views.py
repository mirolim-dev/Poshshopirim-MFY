from django.shortcuts import render

from .models import Post, PostCategory
# Create your views here.

def post(request):
    categories = PostCategory.objects.all()
    posts = Post.objects.prefetch_related('author')
    recent_posts = posts if posts.count() < 6 else posts[-6:]
    context = {
        'categories': categories, 
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog.html', context)


def posts_by_category(request, tag):
    categories = PostCategory.objects.all()
    category = PostCategory.objects.get(name=tag)
    posts = Post.objects.filter(category=category).prefetch_related('author')
    recent_posts = posts if posts.count() < 6 else posts[-6:]
    
    
    context = {
        'categories': categories, 
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog.html', context)


def post_detail(request, pk:int):
    posts = Post.objects.prefetch_related('author')
    categories = PostCategory.objects.all()
    recent_posts = posts if posts.count() < 6 else posts[-6:]
    context = {
        'post': Post.objects.get(id=pk),
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'detail.html', context)
