from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits #+ string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create your models here.
from .permissions import permission_data
class Worker(models.Model):
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['-created_at', 'is_active']
        permissions = permission_data
        
    first_name = models.CharField(max_length=30, verbose_name='Ism')
    last_name = models.CharField(max_length=30, verbose_name="Familya")
    role = models.CharField(max_length=30, verbose_name="Lavozim", null=True)
    phone = models.CharField(max_length=17, verbose_name="Telefon raqam", unique=True, help_text="Ushbu raqam \
        Hodimning tizimga kirishdagi username sifatidaham foydalaniladi")
    password = models.CharField(max_length=10, verbose_name="Parol", help_text="Ushbu parol \
        Xodimning tizimga kirishida ishlatiladi", default=generate_password())
    address = models.CharField(max_length=100, verbose_name="Manzil", 
                               help_text="Masalan: Fayziobod qishlog'i Bog'ibo'ston \
                               ko'chasi 40-uy")
    image = models.ImageField(upload_to='workers/', blank=True, verbose_name="Rasm")
    description = models.TextField(verbose_name="Qisqacha izoh", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
from django.contrib.auth.models import Permission

def give_permissions_to_user(user, permissions, **kwargs):
    permission_ids = [p.id for codename, name in permissions for p in Permission.objects.filter(name__icontains=name).exclude(content_type__app_label='auth')] 
    user.user_permissions.add(*permission_ids)
    
    
@receiver(post_save, sender=Worker)
def create_user(sender, instance, created, **kwargs):
    if created:
        username = f"{instance.first_name} {instance.last_name}"
        user = User.objects.create_user(username=username, password=instance.password, is_staff=True)
        give_permissions_to_user(user, permission_data)