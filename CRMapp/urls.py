from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import SalesHistory, ShowProcessedSales, SendReminder, SendIncidences, IncidencesJSON

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
    url(r'^incidences/$',
        SendIncidences.as_view(),
        name='incidences'),
    url(r'^incidences.json/$',
        IncidencesJSON.as_view(),
        name='incidence_json')

]