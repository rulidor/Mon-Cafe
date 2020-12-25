class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplierDTO):  # insert Supplier DTO
        self._conn.execute(""" INSERT INTO Suppliers VALUES (?, ?,?)
        """, [supplierDTO.id, supplierDTO.name, supplierDTO.contact_information])

    def find(self, id):  # retrieve Supplier DTO
        c = self._conn.cursor()
        c.execute(""" SELECT * FROM Suppliers WHERE id = ?""", [id])
        return Supplier(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT * FROM Suppliers order by id""").fetchall()
        # return [Supplier(*row) for row in all]
        return all