from django.contrib.auth.models import User

from django.db import models
from decimal import Decimal

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(decimal_places=2, max_digits=10, default= Decimal('0.00'))
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='头像')


    def __str__(self):
        return f"{self.user.username} 的扩展信息"
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100, default="/static/img/chenjunjie.jpg")
    intro = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.00)
    def __str__(self):
        return self.title