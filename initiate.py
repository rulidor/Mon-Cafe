import os

# import imp
import atexit
import sys

from DTO.Coffee_stand import Coffee_stand
from DTO.Employee import Employee
from DTO.Product import Product
from DTO.Supplier import Supplier
from _Repository import Repository


def run(cfg_path):
    if os.path.exists('moncafe.db'):
        os.remove('moncafe.db')
    repo = Repository()
    repo.activities.activity_counter = 0
    # creatTables
    repo.create_table()
    # insert into tables

    with open(cfg_path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            splitedLine = line.split(",")
            c = line.split(",")[0]

            if c == 'E':
                repo.employees.insert(Employee(splitedLine[1], splitedLine[2].strip(), splitedLine[3], splitedLine[4]))
            elif c == 'S':
                repo.suppliers.insert(Supplier(splitedLine[1], splitedLine[2].strip(), splitedLine[3][1:].strip("\n")))
            elif c == 'P':
                repo.products.insert(Product(splitedLine[1], splitedLine[2].strip(), splitedLine[3], 0))
            elif c == 'C':
                repo.coffee_stands.insert(Coffee_stand(splitedLine[1], splitedLine[2].strip(), splitedLine[3]))
            line = fp.readline()
            cnt += 1

    # update when exit
    atexit.register(repo._close)


if __name__ == '__main__':
    filepath = sys.argv[1]
    run(filepath)
