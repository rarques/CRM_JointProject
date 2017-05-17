"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from CRMapp.views import *

urlpatterns = [
    url(r'^$', base),
    url(r'^worker/', include('CRMapp.urls', namespace='crm')),
    url(r'^admin/', admin.site.urls),
    url(r'^person_profile/', person_profile, name='person_profile'),
    url(r'^company_profile/', company_profile, name='company_profile'),
    url(r'^modify_person/', modify_person, name='modify_person'),
    url(r'^modify_company/', modify_company, name='modify_company'),
    url(r'^register/$', register, name='register'),
    url(r'^register-person/$', register_person, name='register_person'),
    url(r'^register-company/$', register_company, name='register_company'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/profile/$', modify_person)
]
