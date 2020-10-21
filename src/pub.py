class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}
        self.food_list = []

    def add_drink_to_list(self, drink):
        if drink in self.drinks:
            self.drinks[drink] += 1
        else:
            self.drinks[drink] = 1
        

    def add_food_to_list(self, food):
        self.food_list.append(food)

    def drinks_list_count(self):
        return len(self.drinks)

    def food_list_count(self):
        return len(self.food_list)

    def create_stock(self):
        pass