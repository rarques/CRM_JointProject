from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import SalesHistory, ShowProcessedSales

urlpatterns = [

    url(r'sales/$',
        login_required(SalesHistory.as_view()),
        name='salesdpt'),

    url(r'salesinfo/$',
        login_required(ShowProcessedSales.as_view()),
        name='salesinfo')

]