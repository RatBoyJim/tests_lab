import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Emily Cullen", 20.00)
    

    def test_customer_has_name(self):
        self.assertEqual("Emily Cullen", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        pub = Pub("The Prancing Pony", 100.00)
        # customer = Customer("Michael Anderson", 50.00)
        drink = Drink("Vodka Martini", 6.50)
        pub.add_drink_to_list(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(13.50, self.customer.wallet)


