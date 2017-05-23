from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from CRMapp.models import WebUser, Sale, Product


class Send_new_information:
    def __init__(self, request):
        self.request = request
        self.clients = WebUser.objects.all()
        self.products = Product.objects.all()
        self.sales = Sale.objects.all()


    def return_json(self):
        if self.request.POST.get('clients'):
            return self.return_clients_json()
        elif self.request.POST.get('products'):
            return self.return_products_json()
        elif self.request.POST.get('sales'):
            return self.return_sales_json()

    def return_clients_json(self):
        data = serializers.serialize('json', self.clients)
        return HttpResponse(data, content_type='application/{0}'.format('json'))

    def return_products_json(self):
        data = serializers.serialize('json', self.sales)
        return HttpResponse(data, content_type='application/{0}'.format('json'))

    def return_sales_json(self):
        data = serializers.serialize('json', self.products)
        return HttpResponse(data, content_type='application/{0}'.format('json'))
