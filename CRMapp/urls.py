from django.conf.urls import url
from views import SalesHistory

urlpatterns = [

    url(r'sales/$',
        SalesHistory.as_view(),
        name='salesdpt')

]