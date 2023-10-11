from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import PendingUser


def register(request):
    return render(request, 'aida_admin_app/register.html')

