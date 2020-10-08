from django import forms
from django.core import validators
from django.contrib.auth.models import User
from user_app.models import UserProfile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    v_pw = forms.CharField(label='Verify Password', widget=forms.PasswordInput(attrs={'placeholder': 'Verify password'}))

    def clean(self):
        cleaned_data = super().clean()

        clean_pw = cleaned_data['password']
        clean_vpw = cleaned_data['v_pw']

        if clean_pw != clean_vpw:
            raise forms.ValidationError('Both passwords must match')

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'v_pw')


# class UserProfileForm(forms.ModelForm):
#
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#
#     class Meta():
#         model = UserProfile
#         fields = ('first_name', 'last_name')