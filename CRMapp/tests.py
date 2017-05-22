from django.test import TestCase

from CRMapp.controller.ProcessedData import ProcessedData

from CRMapp.controller.ProcessClients import ProcessClients
from models import *
from CRMapp.models import WebUser, UserAsPerson
from django.contrib.auth.models import User
import json


class ModelsTesting(TestCase):
    def setUp(self):
        user1, user2, user3 = self.create_django_users()

        web_user1, web_user2 = self.create_web_users(user1, user2)

        self.create_person_company_employee(user3, web_user1, web_user2)

        self.create_product()

        Sale.objects.create(client=web_user1, product=Product.objects.get(name="croissant"))
        self.pd = ProcessedData()

    def create_django_users(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        return user1, user2, user3

    def create_web_users(self, user1, user2):
        web_user1 = WebUser.objects.create(django_user=user1, country="Spain", province="Lleida",
                                           city="Cervera", zip_code=25200,
                                           street="Ramon Balcells n2", phone=288)
        web_user2 = WebUser.objects.create(django_user=user2, country="Spain", province="Castamere", city="Rip city",
                                           zip_code=666, street="All water n1",
                                           phone=322)
        return web_user1, web_user2

    def create_product(self):
        category = Category.objects.create(name="menjar")
        Product.objects.create(name="croissant", category=category, price=2)
        Product.objects.create(name="bocata", category=category, price=3)

    def create_person_company_employee(self, user3, web_user1, web_user2):
        UserAsPerson.objects.create(web_user=web_user1, DNI="312W")
        UserAsCompany.objects.create(web_user=web_user2, CIF="12w2")
        Employee.objects.create(django_user=user3, NSS="123N", department="marqueting")

    def test_person_attributes(self):
        user = User.objects.get(username="user1")
        web_user = WebUser.objects.get(django_user=user)
        person = UserAsPerson.objects.get(web_user=web_user)
        self.assertEqual(person.DNI, "312W")

    def test_company_attributes(self):
        user = User.objects.get(username="user2")
        web_user = WebUser.objects.get(django_user=user)
        company = UserAsCompany.objects.get(web_user=web_user)
        self.assertEqual(company.CIF, "12w2")

    def test_employee_attributes(self):
        user = User.objects.get(username="user3")
        employee = Employee.objects.get(django_user=user)
        self.assertEqual(employee.NSS, "123N")
        self.assertEquals(employee.department, "marqueting")

    def test_person_opinion(self):
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=person.web_user, name="maravilla", comment="roto2", rating=5)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 5)

    def test_company_opinion(self):
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Opinion.objects.create(user=company.web_user, name="maravilla", comment="roto2", rating=4)
        opinion = Opinion.objects.get(name="maravilla")
        self.assertEqual(opinion.rating, 4)

    def test_person_incidence(self):
        person = UserAsPerson.objects.get(DNI="312W")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=person.web_user, name="que collons", explanation="lulz",
                                 category="Trencat")
        incidence = Incidence.objects.get(category="Trencat")
        self.assertEqual(incidence.explanation, "lulz")

    def test_company_incidence(self):
        company = UserAsCompany.objects.get(CIF="12w2")
        product = Product.objects.get(name="croissant")
        Incidence.objects.create(user=company.web_user, name="que collons", explanation="lulz",
                                 category="Defectuos")
        incidence = Incidence.objects.get(category="Defectuos")
        self.assertEqual(incidence.explanation, "lulz")

    def test_user_interested_in_categories(self):
        category1 = Category.objects.create(name="ordenador")
        category2 = Category.objects.create(name="components")
        user = WebUser.objects.get(django_user=User.objects.get(username="user1"))
        CategoryPerUser.objects.create(user=user, category=category1)
        CategoryPerUser.objects.create(user=user, category=category2)
        catched_user = CategoryPerUser.objects.get(category=category2)
        self.assertEqual(catched_user.user.phone, 288)
        catched_user = CategoryPerUser.objects.get(category=category1)
        self.assertEqual(catched_user.user.phone, 288)

    def test_interested_users_in_category(self):
        category, user1, user2 = self.creating_category_per_user()
        interested_users = CategoryPerUser.objects.filter(category=category)
        first_user = interested_users.get(user=user1)
        second_user = interested_users.get(user=user2)
        self.assertEqual(first_user.user.phone, 288)
        self.assertEqual(second_user.user.phone, 322)

    def creating_category_per_user(self):
        category = Category.objects.create(name="phone")
        user1 = WebUser.objects.get(django_user=User.objects.get(username="user1"))
        user2 = WebUser.objects.get(django_user=User.objects.get(username="user2"))
        CategoryPerUser.objects.create(user=user1, category=category)
        CategoryPerUser.objects.create(user=user2, category=category)
        return category, user1, user2

    """Starting the controller unit testing"""

    def test_top_clients(self):
        actual = self.pd.get_top_buyers().pop()
        self.assertEqual(actual, "user1   Name:")

    def test_top_products(self):
        actual = self.pd.get_top_products().pop()
        self.assertEqual(actual, "croissant")

    def test_bot_products(self):
        actual = self.pd.get_bot_products().pop()
        self.assertEqual(actual, "bocata")


class Process_clients_test_case(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='used_name', email='used_name')
        user1.set_password('patatapatata1')
        web_user1 = WebUser.objects.create(django_user=user1, country="Mordor",
                                           province="Gorgoroth",
                                           city="Barad dur", zip_code=25200,
                                           street="Ramon Balcells n2", phone=288)
        user1.save()
        web_user1.save()

        category1 = Category.objects.create(name="Slavery")
        category1.save()

        category_per_user1 = CategoryPerUser.objects.create(user=web_user1,
                                                            category=category1)
        category_per_user1.save()

    def test_process_client(self):
        http_request_mock = Process_clients_test_case.HttpRequestMock()
        process_clients_controller = ProcessClients(
            request=http_request_mock)

        process_clients_controller.captureFields()
        process_clients_controller.filter_clients_and_return('json')
        json_data = json.loads(process_clients_controller.data)

        self.assertEqual(http_request_mock.POST['country'],
                         json_data[0]['fields']['country'])
        self.assertEqual(http_request_mock.POST['province'],
                         json_data[0]['fields']['province'])
        self.assertEqual(http_request_mock.POST['city'],
                         json_data[0]['fields']['city'])

    class HttpRequestMock(object):
        def __init__(self):
            self.POST = {'country': 'Mordor', 'province': 'Gorgoroth',
                         'city': 'Barad dur', 'category': 'Slavery'}

