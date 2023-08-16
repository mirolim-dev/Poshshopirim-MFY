from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
# from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip

from .models import Post, PostCategory, ViewedIP
# Create your views here.

def post(request):
    categories = PostCategory.objects.all()
    posts = Post.objects.prefetch_related('author')
    recent_posts = posts if posts.count() < 6 else posts[-6:]
    if request.POST:
        keyword = request.POST.get('keyword')
        if keyword:
            posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).select_related('author').order_by('-published_at')
    context = {
        'categories': categories, 
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog.html', context)


def posts_by_category(request, tag):
    categories = PostCategory.objects.all()
    category = PostCategory.objects.get(name=tag)
    all_posts = Post.objects.select_related('author')
    posts = Post.objects.filter(category=category).select_related('author')
    recent_posts = all_posts if all_posts.count() < 6 else all_posts[-6:]
    if request.POST:
        keyword = request.POST.get('keyword')
        if keyword:
            posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).select_related('author').order_by('-published_at')
    
    context = {
        'categories': categories, 
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog.html', context)


def is_ip_address_counted(post, ip_address):
    """It is belong to post detail"""
    return post.viewedip_set.filter(ip_address=ip_address).exists()

def post_detail(request, pk:int):
    post = get_object_or_404(Post, id=pk)
    client_ip, is_routable = get_client_ip(request)
    if client_ip is not None:
        # Check if the IP address has already been counted for this post
        if not is_ip_address_counted(post, client_ip):
            # Increment the views count and store the IP address
            ViewedIP.objects.create(post=post, ip_address=client_ip)
    posts = Post.objects.prefetch_related('author')
    categories = PostCategory.objects.all()
    recent_posts = posts if posts.count() < 6 else posts[-6:]
    context = {
        'post': post,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'detail.html', context)
