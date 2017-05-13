import requests
import json

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
        
        return self.clients_data