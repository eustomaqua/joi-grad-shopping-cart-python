from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        # self.products = sorted(self.products)[::-1]
        # bulk_start_idx = -1

        bulk_keyword_number = {}

        for i, product in enumerate(self.products):
            discount = 0.00
            if product.product_code.startswith("DIS_10"):
                loyalty_points_earned += (product.price / 10)
                discount = product.price * 0.1
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += (product.price / 15)
                discount = product.price * 0.15
            elif product.product_code.startswith("DIS_20"):
                loyalty_points_earned += (product.price / 20)
                discount = product.price * 0.20
            elif product.product_code.startswith("BULK_BUY_2_GET_1"):
                if product.product_code not in bulk_keyword_number:
                    bulk_keyword_number[product.product_code] = 1
                    loyalty_points_earned += (product.price / 5)
                    discount = 0.00
                elif bulk_keyword_number[product.product_code] == 2:
                    bulk_keyword_number[product.product_code] = 0
                    loyalty_points_earned += 0  # (product.price / 5)
                    discount = product.price
                else:  # notice: bulk_keyword_number[product.product_code] in [1, 0]:
                    bulk_keyword_number[product.product_code] += 1
                    loyalty_points_earned += (product.price / 5)
                    discount = 0.00
            #     bulk_start_idx = i
            #     break
            else:
                loyalty_points_earned += (product.price / 5)
                discount = 0.00
            total_price += product.price - discount
        # BULK_BUY_2_GET_1
        # number_of_products = len(self.products)
        # if bulk_start_idx < 0 or bulk_start_idx >= number_of_products:
        if total_price >= 500.00:
            discount = total_price * 0.05
            total_price -= discount
        return Order(int(loyalty_points_earned), total_price)

    def __str__(self):
        product_list = "".join('%s' % product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
