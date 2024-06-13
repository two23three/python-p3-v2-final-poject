from models.game import Game
from models.category import Category
from models.customer import Customer
from models.user import User
from getpass import getpass
def exit_program():
    print("Goodbye!")
    exit()

def list_games():
    games = Game.get_all()
    for game in games:
        print(game)

def game_by_title():
    title = input("Enter game title: ")
    game = Game.get_game_by_title(title)
    print(game)

def game_by_category():
    category_name = input("Enter game category: ")
    category = Category.get_category_by_name(category_name)
    if category:
        games = Game.get_games_by_category(category.id)
        for game in games:
            print(game)
    else:
        print("Category not found.")

def add_game():
    title = input("Enter game title: ")
    category_name = input("Enter game category: ")
    price = input("Enter game price: ")
    try:
        price = float(price)  # Ensure the price is a float
        game = Game.create_game(title, category_name, price)
        print(game)
    except ValueError:
        print("Invalid price. Please enter a numeric value.")

def add_customer():
    name = input("Enter customer name: ")
    try:
        customer = Customer.create_customer(name)
        print(f"Customer created: {customer}")
    except TypeError as e:
        print(f"Error creating customer: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def customer_buys_game():
     customers = Customer.get_all()
     if not customers:
        print("No customers found. Please add a customer first.")
        return

     print("Select a customer:")
     # Create a dictionary with customer ID as key and customer object as value
     customer_dict = {i + 1: customer for i, customer in enumerate(customers)}
     for i, customer in customer_dict.items():
         print(f"{i}. {customer.name}")
 
     customer_index = int(input("Enter customer number: "))
     selected_customer = customer_dict.get(customer_index)
     if not selected_customer:
         print("Invalid customer selection.")
         return
 
     games = Game.get_all()
     if not games:
         print("No games found. Please add a game first.")
         return
 
     print("Select a game:")
     game_dict = {i + 1: game for i, game in enumerate(games)}
     for i, game in game_dict.items():
         print(f"{i}. {game.title}")
 
     game_index = int(input("Enter game number: "))
     selected_game = game_dict.get(game_index)
     if not selected_game:
         print("Invalid game selection.")
         return
 
     selected_customer.buy_game(selected_game)
     print(f"{selected_customer.name} purchased {selected_game.title}")
 
def user_login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    user = User.login(username, password)
    if user:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password.")
        register_choice = input("Would you like to register? (yes/no): ").strip().lower()
        if register_choice == "yes":
            User.register_user(username, password)
            return user_login()  # Recursive call to try login again after registration
        else:
            return False
def delete_game():
    games = Game.get_all()
    if not games:
        print("No games found. Please add a game first.")
        return

    print("Select a game to delete:")
    for i, game in enumerate(games):
        print(f"{i + 1}. {game.title}")

    game_index = int(input("Enter game number: "))
    selected_game = games[game_index - 1]
    Game.delete_game(selected_game)
    print(f"Game '{selected_game.title}' deleted.")
