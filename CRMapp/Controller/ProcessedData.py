from CRMapp.models import WebUser, Sale, Product


class ProcessedData():
    NUMBER_OF_TOP = 10

    def get_top_buyers(self):
        top_buyers = ["No client"] * self.NUMBER_OF_TOP
        top_buyers_register = [0] * self.NUMBER_OF_TOP
        for client in WebUser.objects.all():
            number_of_sales = len(Sale.objects.filter(client=client))
            if number_of_sales > min(top_buyers_register):
                index_to_modify = top_buyers_register.index(min(top_buyers_register))
                top_buyers.pop(index_to_modify)
                top_buyers_register.pop(index_to_modify)
                top_buyers.append(client.django_user.username)
                top_buyers_register.append(number_of_sales)

        return top_buyers

    def get_top_products(self):
        top_products = ["No product"] * self.NUMBER_OF_TOP
        top_products_register = [0] * self.NUMBER_OF_TOP
        for product in Product.objects.all():
            number_of_sales = len(Sale.objects.filter(product=product))
            if number_of_sales > min(top_products_register):
                index_to_modify = top_products_register.index(min(top_products_register))
                top_products.pop(index_to_modify)
                top_products_register.pop(index_to_modify)
                top_products.append(product.name)
                top_products_register.append(number_of_sales)

        return top_products

