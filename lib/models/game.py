from models.__init__ import CONN, CURSOR
from models.category import Category

class Game:
    def __init__(self, id, title, category_id, price):
        self.id = id
        self._title = title
        self.category_id = category_id
        self.price = price

    @property
    def title(self):
        return self._title  

    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title, str) and 5 <= len(title) <= 50:
                self._title = title
            else:
                raise TypeError("title must be of type str and between 5 and 50 characters")
        else:
            raise AttributeError("title cannot be changed")
    
    def __repr__(self):
        return f"Game(id={self.id}, title={self.title}, category_id={self.category_id}, price={self.price})"
  
    def __str__(self):
        return f"Game: {self.title}, Category: {self.category_id}, Price: {self.price}" 
    
    def drop_table():
        CURSOR.execute("DROP TABLE IF EXISTS games")
        CONN.commit()
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
        """)
        CONN.commit()

    def save(self):
        CURSOR.execute("""
        INSERT INTO games (title, category_id, price)
        VALUES (?, ?, ?)
        """, (self.title, self.category_id, self.price))
        self.id = CURSOR.lastrowid  # Set the id after insertion
        CONN.commit()

    @classmethod
    def create_game(cls, title, category_name, price):
        # Check if the game already exists
        existing_game = cls.get_game_by_title(title)
        if existing_game:
            return existing_game

        # Check if the category exists, if not create it
        category = Category.get_category_by_name(category_name)
        if category is None:
            print(f"Category '{category_name}' not found. Creating new category.")
            category = Category.create_category(category_name)
        print(f"Category found: {category.name}, ID: {category.id}")

        # Create the new game
        game = cls(None, title, category.id, price)
        game.save()
        return game


    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT id, title, category_id, price FROM games")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], title=row[1], category_id=row[2], price=row[3]) for row in rows]
   
    @classmethod
    def get_game_by_title(cls, title):
        CURSOR.execute("SELECT * FROM games WHERE title = ?", (title,))
        game = CURSOR.fetchone()
        if game:
            return cls(*game)  # Return an instance
        return None

    @classmethod
    def get_games_by_category(cls, category_id):
        CURSOR.execute("SELECT * FROM games WHERE category_id = ?", (category_id,))
        games = CURSOR.fetchall()
        return [cls(*game) for game in games]  # Return instances
    
    def get_customers(self):
        CURSOR.execute("""
        SELECT customers.* FROM customers
        JOIN purchases ON customers.id = purchases.customer_id
        WHERE purchases.game_id = ?
        """, (self.id,))
        customers = CURSOR.fetchall()
        return customers
    
    
    def delete_game(self):
        CURSOR.execute("DELETE FROM games WHERE id = ?", (self.id,))
        CONN.commit()
