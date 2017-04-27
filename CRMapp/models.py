from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class WebUser(models.Model):
    django_user = models.Model(User)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postal_code = models.IntegerField()
    street = models.CharField(max_length=50)


class UserAsPerson(models.Model):
    web_user = models.Model(WebUser)


class UserAsCompany(models.Model):
    web_user = models.Model(WebUser)


class WorkerUser(models.Model):
    django_user = models.Model(User)

class Opinion(models.Model):
    user = models.ForeignKey(WebUser)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)


class Incidence(models.Model):
    user = models.ForeignKey(WebUser)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30)