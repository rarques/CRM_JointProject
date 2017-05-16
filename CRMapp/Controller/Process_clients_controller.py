from django.http.response import HttpResponse

from CRMapp.models import WebUser, CategoryPerUser
from django.core import serializers


class Process_clients_controller(object):
    def __init__(self, request, country=None, province=None, city=None, category=None):
        self.request = request
        self.country = country
        self.province = province
        self.city = city
        self.category = category
        self.web_users = []
        self.users = []

    def captureFields(self):
        self.country = self.request.POST['country']
        self.province = self.request.POST['province']
        self.city = self.request.POST['city']
        self.category = self.request.POST.get('category')

    def filter_clients_and_return(self, format):
        web_users = WebUser.objects.all()
        if self.country:
            web_users = WebUser.objects.filter(country=self.country)
        if self.province:
            web_users = web_users.filter(province=self.province)
        if self.city:
            web_users = web_users.filter(city=self.city)

        users = [user.user for user in CategoryPerUser.objects.filter(category=self.category)
                 if user.user in web_users]

        data = serializers.serialize('json', users)
        return HttpResponse(data, content_type='application/{0}'.format(format))
