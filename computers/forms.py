from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Computer

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'surname', 'image', 'signature']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismni kiriting'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familyani kiriting'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'signature': forms.HiddenInput()
        }
        labels = {
            'name': 'Ism',
            'surname': 'Familya',
            'image': 'Rasm',
            'signature': 'Imzo'
        }