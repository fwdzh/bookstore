from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from store.models import UserProfile
for user in User.objects.all():
    UserProfile.objects.get_or_create(user=user)
