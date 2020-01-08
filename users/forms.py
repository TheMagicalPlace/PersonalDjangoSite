from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_joined = timezone.now

    class Meta:
        # nested namespace for configurations, when .save() is called this is saved
        model = User
        fields = ['username','email','password1','password2']