from django.contrib.auth.hashers import make_password
from django.db import models
import uuid


class PendingUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class ApprovedUser(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    system_prompt = models.CharField(max_length=500)

    def __str__(self):
        return self.username


