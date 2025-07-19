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
        fields = ['name', 'surname', 'monitors_count', 'computers_count', 'keyboards_count', 'mice_count', 'image', 'signature']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismni kiriting'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familyani kiriting'
            }),
            'monitors_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Monitorlar sonini kiriting',
                'min': '1',
                'value': '1'
            }),
            'computers_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kompyuterlar sonini kiriting',
                'min': '1',
                'value': '1'
            }),
            'keyboards_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Klaviaturalar sonini kiriting',
                'min': '1',
                'value': '1'
            }),
            'mice_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sichqonchalar sonini kiriting',
                'min': '1',
                'value': '1'
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
            'monitors_count': 'Monitorlar soni',
            'computers_count': 'Kompyuterlar soni',
            'keyboards_count': 'Klaviaturalar soni',
            'mice_count': 'Sichqonchalar soni',
            'image': 'Rasm',
            'signature': 'Imzo'
        }