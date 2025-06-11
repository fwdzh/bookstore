from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100, default="/static/img/chenjunjie.jpg")
    intro = models.TextField()
    def __str__(self):
        return self.title