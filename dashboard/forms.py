from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

