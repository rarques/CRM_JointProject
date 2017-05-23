from datetime import timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from CRMapp.controller.CompanyController import *
from CRMapp.controller.PersonController import *
from CRMapp.controller.ProcessClients import ProcessClients
from CRMapp.controller import Send_new_information
from CRMapp.controller.ProcessedData import ProcessedData
from CRMapp.controller.SalesHistoryProcesser import SalesHistoryProcesser
from CRMapp.controller.Send_new_information import Send_new_information
from CRMapp.models import CategoryPerUser, Category, Employee, Sale, Product
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
            person = PersonController(request.POST)
            new_user = person.create_new_django_user(user_form)
            new_web_user = person.create_new_web_user(web_user_form, new_user)
            person.register_interested_categories(new_web_user, interested_categories)
            person.create_new_user_as_person(user_as_person_form, new_web_user)
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
            company = CompanyController(request.POST)
            new_user = company.create_new_django_user(user_form)
            new_web_user = company.create_new_web_user(web_user_form, new_user)
            company.register_interested_categories(new_web_user, interested_categories)
            company.create_new_company_user(user_as_company_form, new_web_user)
            return HttpResponse("Registered")
        return render(request, 'register.html', {
            "title": "Register as Person",
            "basic_form": user_form,
            "form": web_user_form,
            "specific_form": user_as_company_form,
            "destination_url": "/register-company/"
        })


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
        person = PersonController(request.POST)
        person.update_person_profile(user, web_user, user_as_person)
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
        company = CompanyController(request.POST)
        company.update_company_profile(user, web_user,
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


class SalesHistory(ListView):
    model = Employee
    template_name = 'sales_history.html'
    queryset = ""


class ShowProcessedSales(ListView):
    model = Employee
    template_name = 'processed_sales.html'
    queryset = ""

    def post(self, *args, **kwargs):
        self.save_api_information()
        bot_products, top_buyers, top_products = self.process_sale_data()
        return render(self.request,
                      self.template_name,
                      {
                          'top_buyers': top_buyers,
                          'top_products': top_products,
                          'bot_products': bot_products
                      }
                      )

    def process_sale_data(self):
        processed_data = ProcessedData()
        top_buyers = processed_data.get_top_buyers()
        top_products = processed_data.get_top_products()
        bot_products = processed_data.get_bot_products()
        return bot_products, top_buyers, top_products

    def save_api_information(self):
        sales_processer = SalesHistoryProcesser()
        sales_processer.catch_data()
        sales_processer.process_data()
        sales_processer.save_data()


def process_client_JSON(request):
    if request.method == 'GET':
        return render(request, 'process_client.html', {
            'categories': Category.objects.all()
        })
    elif request.method == 'POST':
        process_clients_controller = ProcessClients(request)
        process_clients_controller.captureFields()
        return process_clients_controller.filter_clients_and_return('json')


@login_required
def purchases_per_user(request):
    user = request.user
    web_user = WebUser.objects.get(django_user=user)
    sales = Sale.objects.filter(client=web_user)

    return render(request, 'sales_list.html', {
        "sales": sales,
    })


@login_required
def register_incidence(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        return render(request, 'register_incidence.html', {
            "product": product,
            "incidence_form": IncidenceForm(),
            "submitted": False,
        })
    elif request.method == 'POST':
        incidence_form = IncidenceForm(request.POST)
        if incidence_form.is_valid():
            incidence = incidence_form.save(commit=False)
            incidence_category = request.POST.get("category")
            sale = Sale.objects.get(id=pk)
            web_user = WebUser.objects.get(django_user=request.user)
            incidence.user = web_user
            incidence.category = incidence_category
            incidence.sale = sale
            incidence.save()
            return render(request, 'register_incidence.html', {
                "submitted": True
            })


@login_required
def post_opinion(request, pk):
    if request.method == 'GET':
        sale = Sale.objects.get(id=pk)
        product = Product.objects.get(sale=sale)
        return render(request, 'post_opinion.html', {
            "product": product,
            "opinion_form": OpinionForm(),
            "submitted": False,
        })
    elif request.method == 'POST':
        opinion_form = OpinionForm(request.POST)
        if opinion_form.is_valid():
            opinion = opinion_form.save(commit=False)
            sale = Sale.objects.get(id=pk)
            product = Product.objects.get(sale=sale)
            web_user = WebUser.objects.get(django_user=request.user)
            if Opinion.objects.filter(sale=sale, user=web_user).exists():
                Opinion.objects.get(sale=sale, user=web_user).delete()
            opinion.user = web_user
            opinion.save()
            sale.opinion = opinion
            sale.save()
            return render(request, 'post_opinion.html', {
                "submitted": True
            })


@login_required
def profile(request):
    web_user = WebUser.objects.filter(django_user=request.user)
    if UserAsPerson.objects.filter(web_user=web_user).exists():
        return redirect(to='../../person_profile/')
    elif UserAsCompany.objects.filter(web_user=web_user).exists():
        return redirect(to='../../company_profile/')


class SendReminder(ListView):
    model = WebUser
    template_name = 'send_reminders.html'

    def post(self, *args, **kwargs):
        remainder_date = datetime.now() - timedelta(days=15)
        notify_clients = list(User.objects.filter(last_login__lt=remainder_date))
        for client in notify_clients:
            send_mail(
                'Technogad Systems',
                'We have new products, come and see them at technogad.herokuapp.com',
                'technogado@gmail.com',
                [client.email]
            )
        return HttpResponse("Users Notified")


class SendRecommendation(ListView):
    model = WebUser
    template_name = 'recommendation.html'

    def get_context_data(self, **kwargs):
        context = super(SendRecommendation, self).get_context_data(**kwargs)
        user = WebUser.objects.get(django_user=self.request.user)
        pd = ProcessedData()
        top_products = pd.get_top_products()
        context['recommended'] = Product.objects.all().first

        if CategoryPerUser.objects.filter(user=user).exists():
            category = CategoryPerUser.objects.get(user=user).category
            for product in top_products:
                if Product.objects.filter(name=product, category=category).exists():
                    context['recommended'] = Product.objects.get(name=product, category=category)

        return context


class SendIncidences(ListView):
    model = Incidence
    template_name = 'incidence_list.html'

    def get_context_data(self, **kwargs):
        context = super(SendIncidences, self).get_context_data(**kwargs)
        incidences = Incidence.objects.all().order_by('category')
        context['incidences'] = incidences
        return context


class IncidencesJSON(View):
    def get(self, request):
        incidences = Incidence.objects.all()
        data = serializers.serialize('json', incidences)
        return HttpResponse(data, content_type='application/json')


class SendOpinions(ListView):
    model = Opinion
    template_name = 'opinion_list.html'

    def get_context_data(self, **kwargs):
        context = super(SendOpinions, self).get_context_data(**kwargs)
        sales_with_opinion = Sale.objects.filter(opinion__isnull=False).order_by('product__name')
        context['sales_with_opinion'] = sales_with_opinion
        return context


class OpinionsJSON(View):
    def get(self, request):
        opinions = Opinion.objects.all()
        data = serializers.serialize('json', opinions)
        return HttpResponse(data, content_type='application/json')

def send_new_information(request):
    send_new_information = Send_new_information(request)
    return render(request=request, template_name='list_information.html', context={
        'clients': send_new_information.clients,
        'sales': send_new_information.sales,
        'products': send_new_information.products
    })


def send_new_information_json(request):
    send_new_information = Send_new_information(request)
    return send_new_information.return_json()

