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

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-date_joined',)
        db_table = 'user'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile/pics/', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    npm = models.CharField(max_length=18, unique=True, blank=True)
    phone_number = models.JSONField(blank=True, default=dict)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('-user',)
        db_table = 'user_profile'
