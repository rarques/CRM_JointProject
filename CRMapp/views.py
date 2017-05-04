# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect

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
        return render_to_response(template_name='person_profile.html',
                                  context={
                                      'user_name': user.username,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
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
        return render_to_response(template_name='company_profile.html',
                                  context={
                                      'user_name': user.username,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
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
    if request.method == 'POST' \
            and request.POST['password'] \
                    == request.POST['repeat_password']:
        parameters = get_person_profile_parameters(request.POST)
        update_person_profile(parameters, user, web_user, user_as_person)
    else:
        return render_to_response(template_name='modify_person.html',
                                  context={
                                      'user_name': user.username,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
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
    return redirect(to='person_profile.html')


@login_required
def modify_company(request):
    """
    Modifies the profile of a user of type company
    :param request: HttpRequest
    """
    user = request.user
    web_user = WebUser.objects.get(django_user=user)
    user_as_company = UserAsCompany.objects.get(web_user=web_user)
    if request.method == 'POST' \
            and request.POST['password'] \
                    == request.POST['repeat_password']:
        parameters = get_company_profile_parameters(request.POST)
        update_company_profile(parameters, user, web_user, user_as_company)
    else:
        return render_to_response(template_name='modify_company.html',
                                  context={
                                      'user_name': user.username,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
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
    return redirect(to='company_profile.html')


def get_company_profile_parameters(source):
    """
    Capture the parameters of the company type user profile
    :param request: HttpRequest
    :return: A dictionary with parameters
    """
    parameters = {}
    get_basic_parameters(parameters, source)
    get_user_parameters(parameters, source)
    get_company_parameters(parameters, source)
    return parameters


def get_person_profile_parameters(source):
    """
    Capture the parameters of the person type user profile
    :param request: HttpRequest
    :return: A dictionary with parameters
    """
    parameters = {}
    get_basic_parameters(parameters, source)
    get_user_parameters(parameters, source)
    get_company_parameters(parameters, source)
    return parameters


def get_basic_parameters(parameters, source):
    """
    Captures the parameters associated with the Django user model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # basic fields
    parameters['user_name'] = source['user_name'] \
        if 'user_name' in source['user_name'] else ''
    parameters['first_name'] = source['first_name'] \
        if 'first_name' in source['first_name'] else ''
    parameters['last_name'] = source['last_name'] \
        if 'last_name' in source['last_name'] else ''
    parameters['email'] = source['email'] \
        if 'email' in source['email'] else ''
    parameters['password'] = source['password'] \
        if 'password' in source['password'] else ''
    parameters['repeat_password'] = source['repeat_password'] \
        if 'repeat_password' in source['repeat_password'] else ''


def get_user_parameters(parameters, source):
    """
    Captures the parameters associated with the WebUser model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # user information
    parameters['country'] = source['country'] \
        if 'country' in source['country'] else ''
    parameters['province'] = source['province'] \
        if 'province' in source['province'] else ''
    parameters['city'] = source['city'] \
        if 'city' in source['city'] else ''
    parameters['zip_code'] = source['zip_code'] \
        if 'zip_code' in source['zip_code'] else ''
    parameters['street'] = source['street'] \
        if 'street' in source['street'] else ''
    parameters['phone'] = source['phone'] \
        if 'phone' in source['phone'] else ''


def get_company_parameters(parameters, source):
    """
    Captures the parameters associated with the UserAsCompany model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # company information
    parameters['cif'] = source['cif'] \
        if 'cif' in source['cif'] else ''


def get_person_parameters(parameters, source):
    """
    Captures the parameters associated with the UserAsPerson model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # company information
    parameters['dni'] = source['dni'] \
        if 'dni' in source['dni'] else ''


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


def update_basic_parameters(parameters, user):
    """
    Updates the parameters associated with the Django user model
    :param parameters: Dictionary that contains all the parameters
    :param user: Django user model
    """
    user.update(username=parameters['user_name'])
    user.update(first_name=parameters['first_name'])
    user.update(last_name=parameters['last_name'])
    user.update(email=parameters['email'])
    user.update(password=parameters['password'])


def update_user_parameters(parameters, web_user):
    """
    Updates the parameters associated with the WebUser model
    :param parameters: Dictionary that contains all the parameters
    :param web_user: WebUser model
    """
    web_user.update(country=parameters['country'])
    web_user.update(province=parameters['province'])
    web_user.update(city=parameters['city'])
    web_user.update(zip_code=parameters['zip_code'])
    web_user.update(street=parameters['street'])
    web_user.update(phone=parameters['phone'])


def update_company_parameters(parameters, user_as_company):
    """
    Updates the parameters associated with the UserAsCompany model
    :param parameters: Dictionary that contains all the parameters
    :param user_as_company: UserAsCompany model
    """
    user_as_company.update(CIF=parameters['cif'])


def update_person_parameters(parameters, user_as_person):
    """
    Updates the parameters associated with the UserAsPerson model
    :param parameters: Dictionary that contains all the parameters
    :param user_as_person: UserAsPerson model
    """
    user_as_person.update(DNI=parameters['dni'])
