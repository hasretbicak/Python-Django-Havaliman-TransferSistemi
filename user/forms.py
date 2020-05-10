from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets ={
            'username'  : TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email'     : EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name' : TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }
CITY=[
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir')
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone'    : TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address'  : TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'city'     : Select(attrs={'class': 'form-control', 'placeholder': 'city'}, choices=CITY),
            'country'  : TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'image'    : FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
        }