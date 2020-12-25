from DTO.Coffee_stand import Coffee_stand


class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_standDTO):
        self._conn.execute("""INSERT INTO Coffee_stands VALUES (?,?,?)""",
                           [coffee_standDTO.id, coffee_standDTO.location, coffee_standDTO.number_of_employees])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Coffee_stands WHERE id = ?""", [id])
        return Coffee_stand(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = (c.execute("""SELECT * FROM Coffee_stands order by id""").fetchall())
        #all = [tuple(filter(None,tp)) for tp in all ]
        # return [Coffee_stand(*row) for row in all]
        # all = tuple(tuple("".join(i.split()) for i in a) for a in all)
        return all;
