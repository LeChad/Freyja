from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=200, label="Email Address",
                             widget=forms.widgets.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Email'
                                 }
                             ))
    username = forms.CharField(required=True, max_length=25, label="Username",
                             widget=forms.widgets.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Username'
                                 }
                             ))
    first_name = forms.CharField(required=True, max_length=100, label="First name",
                             widget=forms.widgets.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First name'
                                 }
                             ))
    last_name = forms.CharField(required=True, max_length=100, label="Last name",
                             widget=forms.widgets.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Last name'
                                 }
                             ))
    password1 = forms.CharField(required=True, label="Password",
                                widget=forms.widgets.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Password'
                                    }
                                ))
    password2 = forms.CharField(required=True, label="Confirm password",
                                widget=forms.widgets.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Confirm password'
                                    }
                                ))

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address is already in use.")
        return email

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
