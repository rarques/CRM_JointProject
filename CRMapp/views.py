from django.http.response import Http404, HttpResponse
from django.shortcuts import render, render_to_response, redirect
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
            "basic_form": UserForm(),
            "form": WebUserForm(),
            "destination_url": "/register-person/"
        })
    elif request.method == 'POST':
        # Register person
        user_form = UserForm(request.POST)
        web_user_form = WebUserForm(request.POST)
        if user_form.is_valid() \
                and web_user_form.is_valid():
            new_user = create_new_django_user(user_form)
            new_web_user = create_new_web_user(web_user_form, new_user)
            # TODO: Create UserAsPerson from web_user
            # return redirect(profile)
            return HttpResponse("Registered")
        else:
            return render(request, 'register.html', {
                "title": "Register as Person",
                "basic_form": user_form,
                # "form": UserAsPersonForm(),
                "destination_url": "/register-person/"
            })


def register_company(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            "title": "Register as Company",
            "basic_form": UserForm(),
            # "form": UserAsCompanyForm(),
            "destination_url": "/register-company/"
        })
    elif request.method == 'POST':
        # Register company
        pass


def create_new_django_user(user_form):
    form_data = user_form.cleaned_data
    new_user = user_form.save(commit=False)
    new_user.set_password(form_data['password'])
    new_user.save()
    return new_user


def create_new_web_user(web_user_form, django_user):
    new_web_user = web_user_form.save(commit=False)
    new_web_user.django_user = django_user
    new_web_user.save()
    return new_web_user
