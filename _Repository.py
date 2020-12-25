import sqlite3

from DAO._Activities import _Activities
from DAO._Coffee_stands import _Coffee_stands
from DAO._Employees import _Employees
from DAO._Products import _Products
from DAO._Suppliers import _Suppliers
from DTO.Activity import Activity


class _Repository:
    _instance = None

    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.employees = _Employees(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.products = _Products(self._conn)
        self.coffee_stands = _Coffee_stands(self._conn)
        self.activities = _Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_table(self):


        self._conn.executescript("""CREATE TABLE IF NOT EXISTS Employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL,
                                    salary REAL NOT NULL, coffee_stand INTEGER REFERENCES Coffee_stands(id));
                                    CREATE TABLE IF NOT EXISTS Suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, contact_information TEXT);
                                    CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY,description TEXT NOT NULL,
                                    price REAL NOT NULL, quantity INTEGER NOT NULL);
                                    CREATE TABLE IF NOT EXISTS Coffee_stands (id INTEGER PRIMARY KEY, location TEXT NOT NULL,
                                    number_of_employees INTEGER);
                                    CREATE TABLE IF NOT EXISTS Activities (product_id INTEGER REFERENCES Products(id),
                                    quantity INTEGER NOT NULL, activator_id INTEGER NOT NULL, date DATE NOT NULL);
                                    """)

    def reflect_transaction(self, actor_id, product_id, amount, date, type):
        product_qun = self.products.find(product_id).quantity

        if type == 'sale':
            if product_qun < abs((int)(amount)) or amount == 0:
                pass
            else:
                self.insert_into_activity(product_qun, product_id, amount, actor_id, date)
        else:
            self.insert_into_activity(product_qun, product_id, amount, actor_id, date)

        pass

    def insert_into_activity(self, product_int, product, amount, actor_id, date):
        amount_num = (int)(amount)
        product_qun = product_int + amount_num
        activ = Activity(product, amount, actor_id, date)
        self.activities.insert(activ)
        c = self._conn.cursor()
        c.execute("""UPDATE Products SET quantity = ? WHERE id = ? """, [product_qun, product])
        self.activities_flag = True

    def generate_employee_report(self):
        # write the join query between employee to activity
        self.employees.get_employee_report()

    def is_activities(self):
        return self.activities_flag


def Repository():
    if _Repository._instance is None:
        _Repository._instance = _Repository()
    return _Repository._instance
