from django.contrib import admin
from .models import Appeal

# Register your models here.

class AppealAdmin(admin.ModelAdmin):
    readonly_fields = ['first_name', "last_name", 'phone', 'address', 'content']
    list_display = ['id', 'first_name', 'last_name', 'phone', 'is_active', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'phone', 'address']

admin.site.register(Appeal, AppealAdmin)