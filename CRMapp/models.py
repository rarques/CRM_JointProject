from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class WebUser(models.Model):
    django_user = models.ForeignKey(User)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)


class UserAsPerson(models.Model):
    web_user = models.ForeignKey(WebUser)
    DNI = models.CharField()


class UserAsCompany(models.Model):
    web_user = models.ForeignKey(WebUser)
    CIF = models.CharField()


class Employee(models.Model):
    django_user = models.ForeignKey(User)
    NSS = models.CharField(max_length=30)
    department = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30)


class Opinion(models.Model):
    user = models.ForeignKey(WebUser)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=200)
    rating = models.IntegerField()
    date = models.DateField(default=now)


class Incidence(models.Model):
    user = models.ForeignKey(WebUser)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)
    explanation = models.TextField(max_length=300)
    category = models.CharField(max_length=30)
    date = models.DateField(default=now)
