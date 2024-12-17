from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.IntegerChoices):
        STUDENT = 0
        LECTURER = 1
        ADMIN = 2

    role = models.IntegerField(null=True, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/pics/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    npm = models.CharField(max_length=18, unique=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
