import requests
import json

from CRMapp.models import Category, WebUser, UserAsPerson, UserAsCompany, Product, Sale
from django.contrib.auth.models import User


class SalesHistoryProcesser():
    def __init__(self):
        self.url = "https://technogad.herokuapp.com/api"
        self.clients_url = self.url + "/v1/clients"
        self.products_url = self.url + "/v1/products"
        self.categories_url = self.url + "/v1/categories"
        self.sales_url = self.url + "/v1/sales"

    def catch_data(self):
        self.clients = requests.get(self.clients_url)
        self.products = requests.get(self.products_url)
        self.categories = requests.get(self.categories_url)
        self.sales = requests.get(self.sales_url)

    def process_data(self):
        self.clients_data = json.loads(self.clients.text)
        self.products_data = json.loads(self.products.text)
        self.categories_data = json.loads(self.categories.text)
        self.sales_data = json.loads(self.sales.text)

    def save_data(self):
        for category in self.categories_data:
            if not Category.objects.filter(name=category["categoryName"]).exists():
                Category.objects.create(name=category["categoryName"])

        for client in self.clients_data:
            if client["clientType"] == "clientType_1":
                if not UserAsPerson.objects.filter(DNI=client["nif"]).exists():
                    UserAsPerson.objects.create(
                        web_user=WebUser.objects.create(
                            django_user=User.objects.create(username=client["idClient"], first_name=client["name"]),
                            country="X", province="X",
                            city="X", zip_code=1,
                            street="X", phone=2),
                        DNI=client["nif"])
            else:
                if not UserAsCompany.objects.filter(CIF=client["nif"]).exists():
                    UserAsCompany.objects.create(
                        web_user=WebUser.objects.create(
                            django_user=User.objects.create(username=client["idClient"], first_name=client["name"]),
                            country="X", province="X",
                            city="X", zip_code=1,
                            street="X", phone=2),
                        CIF=client["nif"])

        for product in self.products_data:
            if not Product.objects.filter(product_code=product["ProductCode"]).exists():
                Product.objects.create(product_code=product["ProductCode"], name=product["productName"],
                                       category=Category.objects.get(name=product["productCategory"]),
                                       price=product["price"])

        for sale in self.sales_data:
            api_date = str(sale["saleDate"])
            unprocessed_date = api_date.split(' ')
            if unprocessed_date[2] == "AM":
                day = unprocessed_date[0].split("/")
                processed_day = day[2] + "-" + day[1] + "-" + day[0]
                processed_date = processed_day + " " + unprocessed_date[1]
            else:
                processed_date = self.change_hours_format(unprocessed_date)

            if UserAsPerson.objects.filter(DNI=sale["client"]).exists():
                Sale.objects.create(client=UserAsPerson.objects.get(DNI=sale["client"]).web_user,
                                    product=Product.objects.get(
                                        product_code=sale["product"]),
                                    date=processed_date)
            elif UserAsCompany.objects.filter(CIF=sale["client"]).exists():
                Sale.objects.create(client=UserAsCompany.objects.get(CIF=sale["client"]).web_user,
                                    product=Product.objects.get(
                                        product_code=sale["product"]),
                                    date=processed_date)

    def change_hours_format(self, unprocessed_date):
        time = unprocessed_date[1]
        time = time.split(":")
        hours = time[0]
        minutes = time[1]
        hours = str(int(hours) + 12)
        day = unprocessed_date[0].split("/")
        processed_day = day[2]+"-"+day[1]+"-"+day[0]
        return processed_day + " " + hours + ":" + minutes
