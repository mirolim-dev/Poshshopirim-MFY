from django.contrib import admin
from .models import PostCategory, Post
from main.models import Worker
# Register your models here.

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['views']
    list_display = ['id', 'author', 'category', 'title', 'views', 'published_at', 'updated_at']
    search_fields = ['title', 'category']
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:  # Only set the author if it's a new instance
    #         user = request.user
    #         worker = Worker.objects.get(phone=user.username)
    #         print(worker)
    #         obj.author = worker
    #     super().save_model(request, obj, form, change)



admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
