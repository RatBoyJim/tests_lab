import unittest
from src.pub import Pub
from src.drink import Drink

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