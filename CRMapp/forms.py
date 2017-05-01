from django.forms import *
from models import *


class UserAsPersonForm(ModelForm):
    class Meta:
        model = UserAsPerson
        fields = ('username', 'DNI')
