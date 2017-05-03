# Create your views here.
from django.contrib.auth.decorators import login_required

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
def person_profile(request, user_id):
    pass


@login_required
def company_profile(request, user_id):
    pass


@login_required
def modify_person(request, user_id):
    pass


@login_required
def modify_company(request, user_id):
    pass
