import unittest
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
    

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_till_has_money(self):
        self.assertEqual(100.00, self.pub.till)

    def test_add_drink_to_list(self):
        drink = Drink("Vodka Martini", 6.50, 3)
        self.pub.add_drink_to_list(drink)
        self.assertEqual(1, self.pub.drinks_list_count())

    def test_add_food_to_list(self):
        food = Food("Mac and cheese", 5.50, 2)
        self.pub.add_food_to_list(food)
        self.assertEqual(1, self.pub.food_list_count())

    def test_stock_count_works(self):
        drink = Drink("Vodka Martini", 6.50, 3)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink)
        self.assertEqual(3, self.pub.drinks[drink])

    def test_stock_value(self):
        drink = Drink("Vodka Martini", 6.50, 3)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink)
        self.assertEqual(13.00, self.pub.stock_value())