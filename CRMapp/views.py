# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from forms import *

from CRMapp.models import WebUser, UserAsPerson, UserAsCompany


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
    user_as_person = UserAsPerson.objects.get(web_user=web_user)
    if request.method == 'POST':
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
    user_as_company = UserAsCompany.objects.get(web_user=web_user)
    if request.method == 'POST':
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
                          'cif': user_as_company.CIF
                      }
                      )
    return redirect(to='../company_profile')


def get_company_profile_parameters(source, user, web_user, user_as_company):
    """
    Capture the parameters of the company type user profile
    :param request: HttpRequest
    :return: A dictionary with parameters
    """
    parameters = {}
    get_basic_parameters(parameters, source, user)
    get_user_parameters(parameters, source, web_user)
    get_company_parameters(parameters, source, user_as_company)
    return parameters


def get_person_profile_parameters(source, user, web_user, user_as_person):
    """
    Capture the parameters of the person type user profile
    :param request: HttpRequest
    :return: A dictionary with parameters
    """
    parameters = {}
    get_basic_parameters(parameters, source, user)
    get_user_parameters(parameters, source, web_user)
    get_person_parameters(parameters, source, user_as_person)
    return parameters


def get_basic_parameters(parameters, source, user):
    """
    Captures the parameters associated with the Django user model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # basic fields
    parameters['username'] = source['username']
    parameters['email'] = source['email']


def get_user_parameters(parameters, source, web_user):
    """
    Captures the parameters associated with the WebUser model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # user information
    parameters['country'] = source['country']
    parameters['province'] = source['province']
    parameters['city'] = source['city']
    parameters['zip_code'] = source['zip_code']
    parameters['street'] = source['street']
    parameters['phone'] = source['phone']

def get_company_parameters(parameters, source, user_as_company):
    """
    Captures the parameters associated with the UserAsCompany model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # company information
    parameters['cif'] = source['cif']


def get_person_parameters(parameters, source, user_as_person):
    """
    Captures the parameters associated with the UserAsPerson model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # company information
    parameters['dni'] = source['dni']


def update_company_profile(parameters, user, web_user, user_as_company):
    """
    Update user profile of company type
    :param parameters: Dictionary that contains all the parameters 
    :param user: Django user model
    :param web_user: WebUser model
    :param user_as_company: UserAsCompany model
    """
    update_basic_parameters(parameters, user)
    update_user_parameters(parameters, web_user)
    update_company_parameters(parameters, user_as_company)
    user.save(update_fields=["username", "email"])
    web_user.save(update_fields=["country", "province", "city", "zip_code",
                                 "street", "phone"])
    user_as_company.save(update_fields=["CIF"])


def update_person_profile(parameters, user, web_user, user_as_person):
    """
    Update user profile of person type
    :param parameters: Dictionary that contains all the parameters
    :param user: Django user model
    :param web_user: WebUser model
    :param user_as_person: user_as_company: UserAsPerson model
    """
    update_basic_parameters(parameters, user)
    update_user_parameters(parameters, web_user)
    update_person_parameters(parameters, user_as_person)
    user.save(update_fields=["username", "email"])
    web_user.save(update_fields=["country", "province", "city", "zip_code",
                                 "street", "phone"])
    user_as_person.save(update_fields=["DNI"])


def update_basic_parameters(parameters, user):
    """
    Updates the parameters associated with the Django user model
    :param parameters: Dictionary that contains all the parameters
    :param user: Django user model
    """
    user.username = parameters['username']
    user.email = parameters['email']


def update_user_parameters(parameters, web_user):
    """
    Updates the parameters associated with the WebUser model
    :param parameters: Dictionary that contains all the parameters
    :param web_user: WebUser model
    """
    web_user.country = parameters['country']
    web_user.province = parameters['province']
    web_user.city = parameters['city']
    web_user.zip_code = parameters['zip_code']
    web_user.street = parameters['street']
    web_user.phone = parameters['phone']


def update_company_parameters(parameters, user_as_company):
    """
    Updates the parameters associated with the UserAsCompany model
    :param parameters: Dictionary that contains all the parameters
    :param user_as_company: UserAsCompany model
    """
    user_as_company.CIF = parameters['cif']


def update_person_parameters(parameters, user_as_person):
    """
    Updates the parameters associated with the UserAsPerson model
    :param parameters: Dictionary that contains all the parameters
    :param user_as_person: UserAsPerson model
    """
    user_as_person.DNI = parameters['dni']


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
            "destination_url": "/register-person/"
        })
    elif request.method == 'POST':
        # Register person
        user_form = UserForm(request.POST)
        web_user_form = WebUserForm(request.POST)
        user_as_person_form = UserAsPersonForm(request.POST)
        if user_form.is_valid() \
                and web_user_form.is_valid() \
                and user_as_person_form.is_valid():
            new_user = create_new_django_user(user_form)
            new_web_user = create_new_web_user(web_user_form, new_user)
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
            "destination_url": "/register-company/"
        })
    elif request.method == 'POST':
        # Register company
        user_form = UserForm(request.POST)
        web_user_form = WebUserForm(request.POST)
        user_as_company_form = UserAsCompanyForm(request.POST)
        if user_form.is_valid() \
                and web_user_form.is_valid() \
                and user_as_company_form.is_valid():
            new_user = create_new_django_user(user_form)
            new_web_user = create_new_web_user(web_user_form, new_user)
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


def create_new_user_as_person(user_as_person_form, web_user):
    new_person_user = user_as_person_form.save(commit=False)
    new_person_user.web_user = web_user
    new_person_user.save()


def create_new_company_user(user_as_company_form, web_user):
    new_company_user = user_as_company_form.save(commit=False)
    new_company_user.web_user = web_user
    new_company_user.save()
