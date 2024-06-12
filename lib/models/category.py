from models.__init__ import CONN, CURSOR

class Category:
    def __init__(self, id, name):
        self.id = id
        self._name = name

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
        INSERT INTO categories (name)
        VALUES (?)
        """, (self.name,))
        self.id = CURSOR.lastrowid  # Get the id of the inserted row
        CONN.commit()

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
        CONN.commit()

    @classmethod
    def create_category(cls, name):
        existing_category = cls.get_category_by_name(name) 
        if existing_category is None:
            category = cls(None, name)
            category.save()
            return category
        else:
            return existing_category
    

    @classmethod
    def get_category_by_name(cls, name):
        CURSOR.execute("SELECT * FROM categories WHERE name = ?", (name,))
        category = CURSOR.fetchone()
        if category:
            return cls(*category)
        else:
            return None
