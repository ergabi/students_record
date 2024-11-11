from django import forms
from django.contrib.auth.models import User
from .models import Reports

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentsReportForm(forms.ModelForm):
    class Meta:  
        model = Reports  
        fields = ['student_name', 'subject', 'mark']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
            'mark': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter mark'}),
        }