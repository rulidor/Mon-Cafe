
class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activityDTO):
        self._conn.execute("""INSERT INTO Activities VALUES (?,?,?,?) """,
                           [activityDTO.product_id, activityDTO.quantity, activityDTO.activator_id, activityDTO.date])

    ####### TODO: check If current product quantity is less than the quantity in the sale. If so - activity the action should be ignored. Do not print any message

    def find_all(self):  # retrieve list of Activity DTOs
        c = self._conn.cursor()
        all = c.execute("""SELECT * FROM Activities order by date """).fetchall()
        return all;



    def activities_reporte(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT date, description,quantity,name as employee_name,suppliers_name from (SELECT date , description, quantity, activator_id, name as suppliers_name from 
(SELECT Activities.date,Products.description, Activities.quantity, Activities.activator_id FROM Activities
LEFT join Products on Activities.product_id = Products.id) as T  LEFT join Suppliers on Suppliers.id = T.activator_id) as P LEFT join Employees on Employees.id = P.activator_id
ORDER by date """).fetchall()
        return all