class Coffee_stand(object):

    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

    def __str__(self):
        return str(self.id) + " " + self.location.strip() + " " + str(self.number_of_employees)