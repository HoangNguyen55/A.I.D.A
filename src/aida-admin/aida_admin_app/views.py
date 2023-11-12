from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'aida_admin_app/base.html')
