from django.db import models
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.contrib import admin

from ckeditor_uploader.fields import RichTextUploadingField

from main.models import Worker

# Create your models here.

class PostCategory(models.Model):
    class Meta:
        verbose_name = "Yangilik Turi"
        verbose_name_plural = "Yangilik Turlari"
        ordering = ['name']
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    def get_all_news(self):
        return self.news_set.all().prefetch_related("author")
    

class Post(models.Model):
    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-published_at']

    author = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Muallif')
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name="Yangilik Turi")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='news/', verbose_name='rasm')
    content = RichTextUploadingField(help_text="Yangilikning kontentini shu yerga yozasiz")
    # views = models.PositiveBigIntegerField(default=0, verbose_name="Ko'rishlar soni")
    
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")

    def __str__(self)->str:
        return self.title
    
    @admin.display(description="Ko'rishlar soni")
    def get_number_of_views(self)->int:
        return self.viewedip_set.all().count()
    
class ViewedIP(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address')
        
    def __str__(self)->str:
        return f"{self.post.title} {self.ip_address}"