from __future__ import absolute_import

import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"


class ShoppingCartTest(unittest.TestCase):
    def test_should_calculate_price_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(100.00, order.total)

    def test_should_calculate_loyalty_points_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(20, order.loyalty_points)

    def test_should_calculate_price_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(90.00, order.total)

    def test_should_calculate_loyalty_points_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)

    def test_should_calculate_price_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(85.00, order.total)

    def test_should_calculate_loyalty_points_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(6, order.loyalty_points)

    def test_should_calculate_price_with_20_percent_discount(self):
        products = [Product(PRICE, "DIS_20_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(80.00, order.total)

    def test_should_calculate_loyalty_points_with_20_percent_discount(self):
        products = [Product(PRICE, "DIS_20_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(5, order.loyalty_points)

    def test_should_calculate_total_with_5_percent_discount(self):
        products = [Product(PRICE * 5, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(475.00, order.total)  # 500*0.05=25

    def test_should_calculate_bulk_buy2get1_discount(self):
        products = [
            Product(PRICE, "BULK_BUY_2_GET_1_ABCD", PRODUCT) for _ in range(3)
        ]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(200.00, order.total)
        self.assertEqual(40, order.loyalty_points)  # 100/5*2

        products = [
            Product(PRICE, "BULK_BUY_2_GET_1_A", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_B", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_C", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_B", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_A", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_A", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_B", PRODUCT),
            Product(PRICE, "BULK_BUY_2_GET_1_A", PRODUCT),
        ]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(570.00, order.total)
        self.assertEqual(120, order.loyalty_points)  # 60+40+20
