from django.contrib import admin

from .models import Book, UserProfile

# Register your models here.
admin.site.register(Book)
admin.site.register(UserProfile)

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'balance')