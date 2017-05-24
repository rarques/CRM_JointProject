from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from views import SalesHistory, ShowProcessedSales, SendReminder, send_new_information, send_new_information_json

urlpatterns = [

    url(r'sales/$',
        login_required(SalesHistory.as_view()),
        name='salesdpt'),

    url(r'salesinfo/$',
        login_required(ShowProcessedSales.as_view()),
        name='salesinfo'),

    url(r'reminder/$',
        login_required(SendReminder.as_view()),
        name='client_reminder'),

    url(r'options/$',
        login_required(ListView.as_view(
            queryset="",
            context_object_name="",
            template_name="list_of_options.html")),
        name='options'),

    url(r'^list_information/$',
        send_new_information,
        name='send_new_information'),


    url(r'^list_information.json',
        send_new_information_json,
        name='send_new_information_json')

]