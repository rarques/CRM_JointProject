from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response, redirect

from CRMapp.Company import *
from CRMapp.Person import *
from CRMapp.User import *
from CRMapp.models import CategoryPerUser, Category
from forms import *


@login_required
def person_profile(request):
    """
    Shows the profile of a user of type person
    :param request: HttpRequest
    :return: Returns the profile template
    """
    if request.method == 'GET':
        user = request.user
        web_user = WebUser.objects.get(django_user=user)
        categories = CategoryPerUser.objects.filter(user=web_user)
        user_as_person = UserAsPerson.objects.get(web_user=web_user)
        return render(request,
                      'person_profile.html',
                      {
                          'username': user.username,
                          'email': user.email,
                          'country': web_user.country,
                          'province': web_user.province,
                          'city': web_user.province,
                          'zip_code': web_user.zip_code,
                          'street': web_user.street,
                          'phone': web_user.phone,
                          'categories': categories,
                          'dni': user_as_person.DNI
                      })


@login_required
def company_profile(request):
    """
    Shows the profile of a user type company
    :param request: HttpRequest
    :return: Returns the profile template
    """
    if request.method == 'GET':
        user = request.user
        web_user = WebUser.objects.get(django_user=user)
        categories = CategoryPerUser.objects.filter(user=web_user)
        user_as_company = UserAsCompany.objects.get(web_user=web_user)
        return render(request,
                      'company_profile.html',
                      {
                          'username': user.username,
                          'email': user.email,
                          'country': web_user.country,
                          'province': web_user.province,
                          'city': web_user.province,
                          'zip_code': web_user.zip_code,
                          'street': web_user.street,
                          'phone': web_user.phone,
                          'categories': categories,
                          'cif': user_as_company.CIF
                      })


@login_required
def modify_person(request):
    """
    Modifies the profile of a user of type person
    :param request: HttpRequest
    """
    user = request.user
    web_user = WebUser.objects.get(django_user=user)
    categories_per_user = Category.objects.all()
    user_as_person = UserAsPerson.objects.get(web_user=web_user)
    if request.method == 'POST':
        CategoryPerUser.objects.filter(user=web_user).delete()
        parameters = get_person_profile_parameters(request.POST,
                                                   user, web_user,
                                                   user_as_person)
        update_person_profile(parameters, user, web_user, user_as_person)
    else:
        return render(request,
                      'modify_person.html',
                      {
                          'username': user.username,
                          'email': user.email,
                          'country': web_user.country,
                          'province': web_user.province,
                          'city': web_user.province,
                          'zip_code': web_user.zip_code,
                          'street': web_user.street,
                          'phone': web_user.phone,
                          'categories': categories_per_user,
                          'dni': user_as_person.DNI
                      }
                      )
    return redirect(to='../person_profile')


@login_required
def modify_company(request):
    """
    Modifies the profile of a user of type company
    :param request: HttpRequest
    """
    user = request.user
    web_user = WebUser.objects.get(django_user=user)
    categories_per_user = Category.objects.all()
    user_as_company = UserAsCompany.objects.get(web_user=web_user)
    if request.method == 'POST':
        CategoryPerUser.objects.filter(user=web_user).delete()
        parameters = get_company_profile_parameters(request.POST,
                                                    user, web_user, user_as_company)
        update_company_profile(parameters, user, web_user,
                               user_as_company)
    else:
        return render(request,
                      'modify_company.html',
                      {
                          'username': user.username,
                          'email': user.email,
                          'country': web_user.country,
                          'province': web_user.province,
                          'city': web_user.province,
                          'zip_code': web_user.zip_code,
                          'street': web_user.street,
                          'phone': web_user.phone,
                          'categories': categories_per_user,
                          'cif': user_as_company.CIF
                      }
                      )
    return redirect(to='../company_profile')


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


