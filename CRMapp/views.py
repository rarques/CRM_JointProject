from django.shortcuts import render, render_to_response
from forms import *


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render_to_response('register.html', {
            "title": "Register",
            "person_form": UserAsPersonForm(),
            "company_form": "Company form"
        })
    else:
        #  Registration process here
        pass
