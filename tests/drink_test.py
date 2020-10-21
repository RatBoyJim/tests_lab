import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Apple Spritz", 5.50)
    

    def test_drink_has_name(self):
        self.assertEqual("Apple Spritz", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.50, self.drink.price)