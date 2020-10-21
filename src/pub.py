class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.food_list = []

    def add_drink_to_list(self, drink):
        self.drinks.append(drink)

    def add_food_to_list(self, food):
        self.food_list.append(food)

    def drinks_list_count(self):
        return len(self.drinks)

    def food_list_count(self):
        return len(self.food_list)