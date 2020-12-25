from DTO.Product import Product


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, productDTO):  # insert Product DTO
        self._conn.execute("""INSERT INTO Products VALUES (?,?,?,?)""",
                           [productDTO.id, productDTO.description, productDTO.price, productDTO.quantity])

    def find(self, id):  # retrieve Product DTO
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Products WHERE id = ?""", [id])
        return Product(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT * FROM Products order by id""").fetchall()
        # return [Product(*row) for row in all]
        return all
