from django.http.response import Http404, HttpResponse
from django.shortcuts import render, render_to_response, redirect

from CRMapp.models import Category, CategoryPerUser
from forms import *


def base(request):
    return render(request, 'base.html',
                  {'PageTitle': 'Base',
                   'TitleHeader': 'Base'})


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
            "specific_form": UserAsPersonForm(),
            "categories": Category.objects.all(),
            "destination_url": "/register-person/"
        })
    elif request.method == 'POST':
        # Register person
        user_form = UserForm(request.POST)
        web_user_form = WebUserForm(request.POST)
        user_as_person_form = UserAsPersonForm(request.POST)
        interested_categories = request.POST.getlist('category')
        if user_form.is_valid() \
                and web_user_form.is_valid() \
                and user_as_person_form.is_valid():
            new_user = create_new_django_user(user_form)
            new_web_user = create_new_web_user(web_user_form, new_user)
            register_interested_categories(new_web_user, interested_categories)
            create_new_user_as_person(user_as_person_form, new_web_user)
            # return redirect(profile)
            return HttpResponse("Registered")
        else:
            return render(request, 'register.html', {
                "title": "Register as Person",
                "basic_form": user_form,
                "form": web_user_form,
                "specific_form": user_as_person_form,
                "destination_url": "/register-person/"
            })


def register_company(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            "title": "Register as Company",
            "basic_form": UserForm(),
            "form": WebUserForm(),
            "specific_form": UserAsCompanyForm(),
            "categories": Category.objects.all(),
            "destination_url": "/register-company/"
        })
    elif request.method == 'POST':
        # Register company
        user_form = UserForm(request.POST)
        web_user_form = WebUserForm(request.POST)
        user_as_company_form = UserAsCompanyForm(request.POST)
        interested_categories = request.POST.getlist('category')
        if user_form.is_valid() \
                and web_user_form.is_valid() \
                and user_as_company_form.is_valid():
            new_user = create_new_django_user(user_form)
            new_web_user = create_new_web_user(web_user_form, new_user)
            register_interested_categories(new_web_user, interested_categories)
            create_new_company_user(user_as_company_form, new_web_user)
            return HttpResponse("Registered")
        return render(request, 'register.html', {
            "title": "Register as Person",
            "basic_form": user_form,
            "form": web_user_form,
            "specific_form": user_as_company_form,
            "destination_url": "/register-company/"
        })


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


def register_interested_categories(new_web_user, interested_categories):
    for cat in interested_categories:
        category = Category.objects.get(name=cat)
        CategoryPerUser.objects.create(user=new_web_user, category=category)


def create_new_user_as_person(user_as_person_form, web_user):
    new_person_user = user_as_person_form.save(commit=False)
    new_person_user.web_user = web_user
    new_person_user.save()


def create_new_company_user(user_as_company_form, web_user):
    new_company_user = user_as_company_form.save(commit=False)
    new_company_user.web_user = web_user
    new_company_user.save()
