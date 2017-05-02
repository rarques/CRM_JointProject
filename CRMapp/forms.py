from django import forms
from .models import *


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = WebUser
        fields = ('django_user', 'country', 'province', 'city', 'zip_code', 'street', 'phone',)