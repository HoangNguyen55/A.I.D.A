from django import forms
from .models import PendingUser


class PendingUserForm(forms.ModelForm):

    class Meta:
        model = PendingUser
        fields = '__all__'

