from models.category import Category
from models.game import Game
from models.customer import Customer
from models.__init__ import CONN, CURSOR

def create_customer_games_table():
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        customer_id INTEGER NOT NULL,
        game_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (game_id) REFERENCES games(id)
    )
    """)
    CONN.commit()
def create_user_table():
    CURSOR.execute("""
 CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
    """)
    CONN.commit()

def drop_purchases_table():
    CURSOR.execute("DROP TABLE IF EXISTS purchases")
    CONN.commit()
                   




def seed_database():
    # Drop tables if they exist
    Category.drop_table()
    Game.drop_table()
    Customer.drop_table()
    drop_purchases_table()
    

    # Create tables
    Category.create_table()
    Game.create_table()
    Customer.create_table()
    create_customer_games_table()
    create_user_table()

    # Create categories and games
    platformer_category = Category.create_category("Platformer")
    game1 = Game.create_game("Super Mario Odyssey", "Platformer", 59.99)
    game2= Game.create_game("The Legend of Zelda: Breath of the Wild", "Action", 59.99)
    game3 = Game.create_game("Super Smash Bros. Ultimate", "Platformer", 59.99)
    if game1:
        print(f"Game created: {game1.title}, ID: {game1.id}, Category ID: {game1.category_id}, Price: {game1.price}")
    else:
        print(f"Game 'Super Mario Odyssey' already exists.")

    # Create customers
   # customer1 = Customer.create_customer("Mansa Musa")
   # print(f"Customer created: {customer1.name}, ID: {customer1.id}, Timestamp: {customer1.timestamp}")

    # Customer buys game
    #customer1.buy_game(game1)
   # print(f"Customer {customer1.name} bought game {game1.title}")

seed_database()
