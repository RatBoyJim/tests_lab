class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, drink, pub):
        #check drink in list
        #check cust has money
        #check cust age
        #if all good remove cust money from wallet and add to pub till
        for item in pub.drinks:
            if item.name == drink.name and self.wallet >= item.price:
                self.wallet -= item.price
                pub.till += item.price