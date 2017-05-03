# coding=utf-8

from django.forms import *
from django.contrib.auth.models import User
from models import WebUser, UserAsPerson


class UserForm(ModelForm):
    password = CharField(max_length=30, widget=PasswordInput)
    repassword = CharField(max_length=30, widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")

        if password != repassword:
            raise forms.ValidationError(
                "password and repassword does not match"
            )


class WebUserForm(ModelForm):
    class Meta:
        model = WebUser
        exclude = ['django_user']

    def clean(self):
        return super(WebUserForm, self).clean()


class UserAsPersonForm(ModelForm):
    class Meta:
        model = UserAsPerson
        exclude = ['web_user']

    def clean(self):
        return super(UserAsPersonForm, self).clean()
