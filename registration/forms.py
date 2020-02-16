from django import forms
import re
# from django.contrib.auth.models import User 
# from django.contrib.auth import get_user_model
from . models import User
class SignupForm(forms.Form):
    username=forms.CharField(label='Username:',help_text="Remember your username. It will be needed for signing in!")
    email=forms.EmailField(label='Email:')
    password=forms.CharField(widget=forms.PasswordInput(),label='Password:',help_text="Your password must contain at least 8 characters and should not be entirely numeric.")
    confirm_password=forms.CharField(widget=forms.PasswordInput(), label='Confirm Password:')

    
    def clean(self):
        cleaned_data=super(SignupForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password should match")
        return cleaned_data

    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        email_exists=User.objects.filter(email=email)
        if email_exists:
            raise forms.ValidationError("{} already exists".format(email))
        return email.lower()

    def clean_username(self):
        username=self.cleaned_data['username']
        username_exists=User.objects.filter(username__iexact=username)
        if username_exists:
            raise forms.ValidationError("{} already exists".format(username))
        return username
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("password is too short!")
        if password.isdigit():
            raise forms.ValidationError('Your password should contain letters!')
        return password




