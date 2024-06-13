import datetime
from models.__init__ import CONN, CURSOR

class Customer:
    def __init__(self, id, name, timestamp = None):
        self.id = id
        self._name = name
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, '_name'):
            if isinstance(name, str) and 5 <= len(name) <= 50:
                self._name = name
            else:
                raise TypeError("name must be of type str and between 5 and 50 characters")
        else:
            raise AttributeError("name cannot be changed")

    def save(self):
        CURSOR.execute("""
        INSERT INTO customers (name, timestamp)
        VALUES (?, ?)
        """, (self.name, self.timestamp))
        self.id = CURSOR.lastrowid  # Set the id after insertion
        CONN.commit()
    
    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, timestamp={self.timestamp})"
    
    def __str__(self):
        return f"Customer: {self.name}, Timestamp: {self.timestamp}"
    def drop_table():
        CURSOR.execute("DROP TABLE IF EXISTS customers")
        CONN.commit()

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
        """)
        CONN.commit()

    @classmethod
    def create_customer(cls, name, ):
        customer = cls(None, name, )
        customer.save()
        return customer

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT id, name, timestamp FROM customers")
        
        rows = CURSOR.fetchall()
        #this is a list of Customer objects
        #Each  object is a tuple of (id, name, timestamp)
        return [cls(id=row[0], name=row[1], timestamp=row[2]) for row in rows]


    def buy_game(self, game):
        CURSOR.execute("""
        INSERT INTO purchases (customer_id, game_id)
        VALUES (?, ?)
        """, (self.id, game.id))
        CONN.commit()
    