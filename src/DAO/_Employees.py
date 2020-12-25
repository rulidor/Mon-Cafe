import sqlite3
from DTO.Employee import Employee


class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employeeDTO):  # insert Employee DTO
        self._conn.execute("""INSERT INTO Employees VALUES (?,?,?,?)""",
                           [employeeDTO.id, employeeDTO.name, employeeDTO.salary, employeeDTO.coffee_stand])

    def find(self, id):  # retrieve Employee DTO
        c = self._conn.cursor()
        c.execute(""" SELECT * FROM Employees WHERE id = ?""", [id])
        return Employee(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT * FROM Employees order by id""").fetchall()
        # return [Employee(*row) for row in all]
        return all

    def get_employee_report(self):
        c = self._conn.cursor()
        sells = c.execute("""SELECT n,s,location, sum(CASE WHEN quan<0 then quan*(-price) else 0 end)as total from (SELECT eid, name as n,salary as s,location,quan,price from
(select eid, name,salary,location,quantity as quan, product_id  from 
(SELECT employees.id as eid, employees.name , employees.salary , Coffee_stands.location 
FROM employees INNER JOIN  Coffee_stands on employees.coffee_stand = Coffee_stands.id) as T
LEFT JOIN Activities on T.eid = Activities.activator_id) as P left join products on P.product_id =products.id order by id)
group by eid""").fetchall()
        count = 0
        for line in sells:
            if count != 0:
                print()
            for t in line:
               print(t, end= " ")
            count = count+1

        print()
        

