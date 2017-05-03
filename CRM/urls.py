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
from os import name

from django.conf.urls import url
from django.contrib import admin
from CRMapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^person_profile/([0-9]+)', person_profile, name='person_profile'),
    url(r'^company_profile([0-9]+)', company_profile, name='company_profile'),
    url(r'^modify_person/([0-9]+)', modify_person, name='modify_person'),
    url(r'^modify_company/([0-9]+)', modify_company, name='modify_company')
]
