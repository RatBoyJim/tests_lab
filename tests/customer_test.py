import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Emily Cullen", 150.00, 28)
    

    def test_customer_has_name(self):
        self.assertEqual("Emily Cullen", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(150.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(28, self.customer.age)

    def test_customer_can_buy_drink(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        pub.add_drink_to_list(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(143.50, self.customer.wallet)

    def test_customer_is_refused_service_underage(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        self.customer = Customer("Emily Cullen", 20.00, 17)
        pub.add_drink_to_list(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(100, pub.till)
        

    def test_customer_can_buy_drink_add_money_to_pub(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        pub.add_drink_to_list(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(106.50, pub.till)

    def test_customer_drunkenness_goes_up(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        pub.add_drink_to_list(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(3, self.customer.drunkenness)

    def test_customer_drunkenness_goes_up(self):
            pub = Pub("The Prancing Pony", 100.00)
            drink = Drink("Vodka Martini", 6.50, 3)
            pub.add_drink_to_list(drink)
            self.customer.buy_drink(drink, pub)
            self.customer.buy_drink(drink, pub)
            self.customer.buy_drink(drink, pub)
            self.customer.buy_drink(drink, pub)
            self.customer.buy_drink(drink, pub)
            self.customer.buy_drink(drink, pub)
            self.assertEqual(117.50, self.customer.wallet)
        

    
    


