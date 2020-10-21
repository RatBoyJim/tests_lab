class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink_to_list(self, drink):
        self.drinks.append(drink)

    def drinks_list_count(self):
        return len(self.drinks)