from django.test import TestCase
from models import *


class simpleTest(TestCase):
    """Simple test to check if CircleCI runs tests correctly"""

    def setUp(self):
        pass

    def test(self):
        self.assertEqual(True, True)


class ModelsTesting(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")

        web_user1 = WebUser.objects.create(django_user=user1, country="Spain", province="Lleida", city="Cervera",
                                           zip_code=25200, street="Ramon Balcells n2",
                                           phone=288)
        web_user2 = WebUser.objects.create(django_user=user2, country="Spain", province="Castamere", city="Rip city",
                                           zip_code=666, street="All water n1",
                                           phone=288)
        UserAsPerson.objects.create(web_user=web_user1, DNI="312W")
        UserAsCompany.objects.create(web_user=web_user2, CIF="12w2")

        Employee.objects.create(django_user=user3, NSS="123N", department="marqueting")
