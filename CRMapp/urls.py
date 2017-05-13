from django.conf.urls import url
from views import SalesHistory, ShowProcessedSales

urlpatterns = [

    url(r'sales/$',
        SalesHistory.as_view(),
        name='salesdpt'),

    url(r'salesinfo/$',
        ShowProcessedSales.as_view())

]