from django.shortcuts import render, render_to_response


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render_to_response('register.html', {
            "person_form": "Person form",
            "company_form": "Company form"
        })
    else:
        #  Registration process here
        pass
