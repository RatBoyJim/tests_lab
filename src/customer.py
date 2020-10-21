class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink, pub):
        #check drink in list
        #check cust has money
        #check cust age
        #if all good remove cust money from wallet and add to pub till
        for item in pub.drinks:
            if item.name == drink.name and self.wallet >= item.price and self.age >= 18 and self.drunkenness < 15:
                self.wallet -= item.price
                pub.till += item.price
                self.drunkenness += item.alcohol_level

    def buy_food(self, food, pub):
        #check drink in list
        #check cust has money
        #check cust age
        #if all good remove cust money from wallet and add to pub till
        for item in pub.food_list:
            if item.name == food.name and self.wallet >= item.price:
                self.wallet -= item.price
                pub.till += item.price
                if (self.drunkenness - item.rejuvenation_level) > 0:
                    self.drunkenness -= item.rejuvenation_level
                else:
                    self.drunkenness = 0


