class Employee(object):

    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.salary) + " " + str(self.coffee_stand)