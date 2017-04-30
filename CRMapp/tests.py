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
        UserAsPerson.objects.create(username="user1", country="Spain", province="Lleida", city="Cervera",
                                    zip_code=25200, street="Ramon Balcells n2",
                                    phone=288, DNI="312W")

        UserAsCompany.objects.create(username="user2", country="Spain", province="Castamere", city="Rip city",
                                     zip_code=666, street="All water n1",
                                     phone=288, CIF="12w2")

        Employee.objects.create(username="user3", NSS="123N", department="marqueting")

        Product.objects.create(name="croissant")


    def test_person_attributes(self):
        """Testing if correct attributes are given when a person is searched"""
        person = UserAsPerson.objects.get(username="user1")
        self.assertEqual(person.DNI, "312W")

    def test_company_attributes(self):
        """Testing if correct attributes are given when a company is searched"""
        company = UserAsCompany.objects.get(username="user2")
        self.assertEqual(company.CIF, "12w2")

    def test_employee_attributes(self):
        """Testing if correct attributes are given when an employee is searched"""
        employee = Employee.objects.get(username="user3")
        self.assertEqual(employee.NSS, "123N")
        self.assertEquals(employee.department, "marqueting")

    def test_person_opinion(self):
        """Person opinion about a product"""
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=person, product=product, name="maravilla", comment="roto2", rating=5)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 5)

    def test_company_opinion(self):
        """Company opinion about a product"""
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=company, product=product, name="maravilla", comment="roto2", rating=4)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 4)

    def test_person_incidence(self):
        """Testing person incidence and getting it using the category"""
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=person, product=product, name="que collons", explanation="lulz",
                                 category="Trencat")
        incidence = Incidence.objects.get(category="Trencat")
        self.assertEqual(incidence.explanation, "lulz")

    def test_company_incidence(self):
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=company, product=product, name="que collons", explanation="lulz",
                                 category="Defectuos")
        incidence = Incidence.objects.get(category="Defectuos")
        self.assertEqual(incidence.explanation, "lulz")
