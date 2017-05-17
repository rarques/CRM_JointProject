from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __unicode__(self):
        return self.name


class WebUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.django_user.username


class CategoryPerUser(models.Model):
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.django_user.username + "   " + self.category.name


class UserAsPerson(models.Model):
    web_user = models.OneToOneField(WebUser, on_delete=models.CASCADE)
    DNI = models.CharField(max_length=30)

    def __unicode__(self):
        return self.DNI


class UserAsCompany(models.Model):
    web_user = models.OneToOneField(WebUser, on_delete=models.CASCADE)
    CIF = models.CharField(max_length=30)

    def __unicode__(self):
        return self.CIF


class Employee(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    NSS = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __unicode__(self):
        return self.django_user.username


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    '''This parameter is optional because it is used only for the company API connection'''
    product_code = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Opinion(models.Model):
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=200)
    rating = models.IntegerField()
    date = models.DateField(default=now)

    def __unicode__(self):
        return self.name


class Incidence(models.Model):
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    explanation = models.TextField(max_length=300)
    category = models.CharField(max_length=30)
    date = models.DateField(default=now)

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    client = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    opinion = models.ForeignKey(Opinion, blank=True, null=True)
    incidence = models.ForeignKey(Incidence, blank=True, null=True)
