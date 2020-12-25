class Activity(object):

    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

    def __str__(self):
        return str(self.product_id) + " " + str(self.quantity) + " " + str(self.activator_id) + " " + str(self.date)