import unittest
from src.customer import Customer
from src.pub import Pub
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Pizza", 7.20, 3)

    def food_has_name(self):
        self.assertEqual("Pizza", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(7.20, self.food.price)

    def test_customer_has_r_l(self):
        self.assertEqual(3, self.food.rejuvenation_level)