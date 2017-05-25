# coding=utf-8

from django.contrib.auth.models import User
from django.forms import *
from django.utils.translation import gettext_lazy as _

from models import WebUser, UserAsPerson, UserAsCompany, Incidence, Opinion


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


class UserAsCompanyForm(ModelForm):
    class Meta:
        model = UserAsCompany
        exclude = ['web_user']

    def clean(self):
        return super(UserAsCompanyForm, self).clean()


class IncidenceForm(ModelForm):
    class Meta:
        model = Incidence
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'explanation': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": _("Title of the incidence   ")
        }
        exclude = ['user', 'product', 'category', 'sale', 'date']

    def clean(self):
        return super(IncidenceForm, self).clean()

class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        exclude = ['user', 'product', 'date']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'comment': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": _("Title of the opinion")
        }

    def clean(self):
        return super(OpinionForm, self).clean()