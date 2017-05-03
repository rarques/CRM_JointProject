# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from CRMapp.models import WebUser, UserAsPerson, UserAsCompany

"""# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
    """


@login_required
def person_profile(request):
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
    if request.method == 'GET':
        user = request.user
        web_user = WebUser.objects.get(django_user=user)
        user_as_company = UserAsCompany.objects.get(web_user=web_user)
        return render_to_response(template_name='company_profile.html.html',
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
    pass


@login_required
def modify_company(request):
    pass
