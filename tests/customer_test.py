import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Emily Cullen", 20.00)
    

    def test_customer_has_name(self):
        self.assertEqual("Emily Cullen", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)