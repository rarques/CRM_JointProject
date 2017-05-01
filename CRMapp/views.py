from django.shortcuts import render, render_to_response
from forms import *


# Create your views here.
def register(request):
    return render_to_response('register.html', {
        "title": "Register",
    })


def register_person(request):
    if request.method == 'GET':
        return render_to_response('register.html', {
            "title": "Register as Person",
            "form": UserAsPersonForm(),
        })
    elif request.method == 'POST':
        # Register person
        pass


def register_company(request):
    if request.method == 'GET':
        return render_to_response('register.html', {
            "title": "Register as Company",
            "form": UserAsCompanyForm(),
        })

    elif request.method == 'POST':
        # Register company
        pass
