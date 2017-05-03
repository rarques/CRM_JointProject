from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __unicode__(self):
        return self.name


class Client(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    number_identificator = models.CharField(max_length=30)
    interested_category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.django_user.username+"  "+self.interested_category.name


class Employee(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    NSS = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __unicode__(self):
        return self.django_user.username


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    price = models.IntegerField()
    price_after_discount = models.IntegerField()
    data_discount_expires = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Opinion(models.Model):
    user = models.ForeignKey(Client)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=200)
    rating = models.IntegerField()
    date = models.DateField(default=now)

    def __unicode__(self):
        return self.name


class Incidence(models.Model):
    user = models.ForeignKey(Client)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=30)
    explanation = models.TextField(max_length=300)
    category = models.CharField(max_length=30)
    date = models.DateField(default=now)

    def __unicode__(self):
        return self.name