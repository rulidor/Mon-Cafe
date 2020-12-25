import atexit

from _Repository import Repository
import os


def doprint():
    repo = Repository()
    print("Activities")
    print_a_list(repo.activities.find_all())


    print("Coffee stands")
    print_a_list(repo.coffee_stands.find_all())

    print("Employees")
    print_a_list(repo.employees.find_all())

    print("Products")
    print_a_list(repo.products.find_all())

    print("Suppliers")
    print_a_list(repo.suppliers.find_all())

    print()
    print("Employees report")
    repo.generate_employee_report()

    ##TODO: check if there are activities. if yes - print them
    c = repo._conn.cursor()
    flag = c.execute("""SELECT count(*) from Activities""").fetchone()[0]
    if flag >0 :
        print()
        print("Activities")
        print_a_list(repo.activities.activities_reporte())

    # update when exit
    atexit.register(repo._close)


def print_a_list(list):
    for item in list:
        print(item)


if __name__ == '__main__':
    doprint()
