# Generated by Django 5.2.2 on 2025-06-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img_url',
            field=models.CharField(default='/static/img/chenjunjie.jpg', max_length=100),
        ),
    ]
