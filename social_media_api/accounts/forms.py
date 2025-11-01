from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'password', 'bio')

class D():
    pass