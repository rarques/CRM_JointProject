# coding=utf-8

from django.forms import *


class BasicForm(Form):
    username = CharField(label='Usuari', max_length=30)
    password = CharField(label='Contrassenya', max_length=50)
    repassword = CharField(label='Confirmació contrassenya', max_length=50)
    email = EmailField(label='E-mail', max_length=50)
    phone = CharField(label='Telèfon', max_length=50)
    street = CharField(label='Carrer', max_length=50)
    city = CharField(label='Ciutat', max_length=30)
    zipcode = CharField(label='Codi postal', max_length=10)
    province = CharField(label='Província', max_length=30)
    country = CharField(label='País', max_length=30)


class UserAsPersonForm(Form):
    dni = CharField(label='DNI', max_length=30)


class UserAsCompanyForm(Form):
    cif = IntegerField(label='CIF')
