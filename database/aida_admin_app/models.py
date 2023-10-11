from django.contrib.auth.hashers import make_password
from django.db import models


class PendingUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


