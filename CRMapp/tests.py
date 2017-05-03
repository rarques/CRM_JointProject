from django.test import TestCase
from models import *


class ModelsTesting(TestCase):
    def setUp(self):
        user1, user2 = self.create_django_users()

        self.create_web_users(user1, user2)

        self.create_product()

    def create_django_users(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user3")
        return user1, user2

    def create_web_users(self, user1, user2):
        category = Category.objects.create(name="Tractor")
        Client.objects.create(django_user=user1, country="Spain", province="Lleida", city="Cervera",
                                          zip_code=25200, street="Ramon Balcells n2",
                                          phone=288, number_identificator="312W", interested_category=category)
        Employee.objects.create(django_user=user2, NSS="123N", department="marqueting")

    def create_product(self):
        category = Category.objects.create(name="menjar")
        Product.objects.create(name="croissant", category=category, price=2, price_after_discount=1)

    def test_client_attributes(self):
        """Testing if correct attributes are given when a person is searched"""
        user = User.objects.get(username="user1")
        client = Client.objects.get(django_user=user)
        self.assertEqual(client.number_identificator, "312W")

    def test_employee_attributes(self):
        """Testing if correct attributes are given when an employee is searched"""
        user = User.objects.get(username="user3")
        employee = Employee.objects.get(django_user=user)
        self.assertEqual(employee.NSS, "123N")
        self.assertEquals(employee.department, "marqueting")

    def test_client_opinion(self):
        """Person opinion about a product"""
        client = Client.objects.get(number_identificator="312W")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=client, product=product, name="maravilla", comment="roto2", rating=5)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 5)

    def test_person_incidence(self):
        """Testing person incidence and getting it using the category"""
        client = Client.objects.get(number_identificator="312W")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=client, product=product, name="que collons", explanation="lulz",
                                 category="Trencat")
        incidence = Incidence.objects.get(category="Trencat")
        self.assertEqual(incidence.explanation, "lulz")

    """Test add category into a client"""
