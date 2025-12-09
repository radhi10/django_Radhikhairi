from django import forms
from .models import Mahasiswa


class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'npm', 'email', 'jurusan', 'nohp']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nama lengkap'
            }),
            'npm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'NPM (mis. 12345678)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@domain.com'
            }),
            'jurusan': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jurusan'
            }),
            'nohp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '08xxxxxxxx'
            }),
        }
