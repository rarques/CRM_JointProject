from django.test import TestCase
from models import *


class ModelsTesting(TestCase):
    def setUp(self):
        user1, user2, user3 = self.create_django_users()

        web_user1, web_user2 = self.create_web_users(user1, user2)

        self.create_person_company_employee(user3, web_user1, web_user2)

        Product.objects.create(name="croissant")

    def create_django_users(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        return user1, user2, user3

    def create_web_users(self, user1, user2):
        web_user1 = WebUser.objects.create(django_user=user1, country="Spain", province="Lleida", city="Cervera",
                                           zip_code=25200, street="Ramon Balcells n2",
                                           phone=288)
        web_user2 = WebUser.objects.create(django_user=user2, country="Spain", province="Castamere", city="Rip city",
                                           zip_code=666, street="All water n1",
                                           phone=288)
        return web_user1, web_user2

    def create_person_company_employee(self, user3, web_user1, web_user2):
        UserAsPerson.objects.create(web_user=web_user1, DNI="312W")
        UserAsCompany.objects.create(web_user=web_user2, CIF="12w2")
        Employee.objects.create(django_user=user3, NSS="123N", department="marqueting")

    def test_person_attributes(self):
        """Testing if correct attributes are given when a person is searched"""
        user = User.objects.get(username="user1")
        web_user = WebUser.objects.get(django_user=user)
        person = UserAsPerson.objects.get(web_user=web_user)
        self.assertEqual(person.DNI, "312W")

    def test_company_attributes(self):
        """Testing if correct attributes are given when a company is searched"""
        user = User.objects.get(username="user2")
        web_user = WebUser.objects.get(django_user=user)
        company = UserAsCompany.objects.get(web_user=web_user)
        self.assertEqual(company.CIF, "12w2")

    def test_employee_attributes(self):
        """Testing if correct attributes are given when an employee is searched"""
        user = User.objects.get(username="user3")
        employee = Employee.objects.get(django_user=user)
        self.assertEqual(employee.NSS, "123N")
        self.assertEquals(employee.department, "marqueting")

    def test_person_opinion(self):
        """Person opinion about a product"""
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=person.web_user, product=product, name="maravilla", comment="roto2", rating=5)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 5)

    def test_company_opinion(self):
        """Company opinion about a product"""
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=company.web_user, product=product, name="maravilla", comment="roto2", rating=4)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 4)

    def test_person_incidence(self):
        """Testing person incidence and getting it using the category"""
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=person.web_user, product=product, name="que collons", explanation="lulz",
                                 category="Trencat")
        incidence = Incidence.objects.get(category="Trencat")
        self.assertEqual(incidence.explanation, "lulz")

    def test_company_incidence(self):
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=company.web_user, product=product, name="que collons", explanation="lulz",
                                 category="Defectuos")
        incidence = Incidence.objects.get(category="Defectuos")
        self.assertEqual(incidence.explanation, "lulz")
