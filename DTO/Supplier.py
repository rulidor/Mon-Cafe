
class Supplier(object):

    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.contact_information
