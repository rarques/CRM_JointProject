from django.shortcuts import render, render_to_response
from forms import *


# Create your views here.
def register(request):
    return render_to_response('register.html', {
        "title": "Register as a Person or as a Company",
    })


def register_person(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            "title": "Register as Person",
            "basic_form": BasicForm(),
            "form": UserAsPersonForm(),
        })
    elif request.method == 'POST':
        # Register person
        pass


def register_company(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            "title": "Register as Company",
            "basic_form": BasicForm(),
            "form": UserAsCompanyForm(),
        })
    elif request.method == 'POST':
        # Register company
        pass
