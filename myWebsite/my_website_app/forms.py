from django import forms
from django.core import validators
from my_website_app.models import UserEnquiries


class UserEnquiriesForm(forms.ModelForm):
    message = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={'cols': 100, 'rows': 5}))
    class Meta:
        model = UserEnquiries
        fields = '__all__'

