from django.db import models

# Create your models here.
class Appeal(models.Model):
    class Meta:
        verbose_name = "Aholi Murojati"
        verbose_name_plural = "Aholi murojatlari"
        ordering = ['is_active', '-created_at']
    first_name = models.CharField(max_length=30, verbose_name="Ism")
    last_name = models.CharField(max_length=30, verbose_name="Familya")
    phone = models.CharField(max_length=17, verbose_name="Telefon")
    address = models.CharField(max_length=100, verbose_name="Manzil")
    content = models.TextField(verbose_name="Murojat", help_text="Murojat shu yerga yozilgan")
    is_active = models.BooleanField(default=False, verbose_name="Murojatchi bilan bog'lanildi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Murojat vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")
    
    def __str__(self)->str:
        return f"{self.first_name} {self.last_name}"
    

        
