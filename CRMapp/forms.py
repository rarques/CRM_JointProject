from django.forms import *
from models import *


class UserAsPersonForm(Form):
    dni = CharField(label='DNI', max_length=30)


class UserAsCompanyForm(Form):
    cif = IntegerField(label='CIF')
