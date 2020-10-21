import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

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

    def test_customer_refused_service_too_drunk(self):
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

    def test_customer_drunkenness_goes_down_with_food(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        food = Food("Pizza", 7.20, 3)
        pub.add_drink_to_list(drink)
        pub.add_food_to_list(food)
        self.customer.buy_drink(drink, pub)
        self.customer.buy_drink(drink, pub)
        self.customer.buy_food(food, pub)
        self.assertEqual(3, self.customer.drunkenness)

    def test_customer_drunkenness_doesnt_go_below_zero(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("Vodka Martini", 6.50, 3)
        food = Food("Sunday Roast", 8.20, 8)
        pub.add_drink_to_list(drink)
        pub.add_food_to_list(food)
        self.customer.buy_drink(drink, pub)
        self.customer.buy_food(food, pub)
        self.assertEqual(0, self.customer.drunkenness)
        

    
    


