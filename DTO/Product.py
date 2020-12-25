class Product(object):

    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str(self.id) + " " + self.description + " " + str(self.price) + " " + str(self.quantity)