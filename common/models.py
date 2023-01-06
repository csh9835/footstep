from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    blogname = models.CharField(max_length=50, blank=True, null=True)
    introduce = models.CharField(max_length=50, blank=True, null=True)