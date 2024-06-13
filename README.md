# GAMEEA Project

## Introduction
GAMEEA is a game store management application designed to streamline the process of managing users, customers, games, purchases, and game categories. It features a command-line interface (CLI) that allows administrators to perform tasks such as adding new games, managing customer information, and processing purchases efficiently. With a well-organized database structure and intuitive user prompts, GAMEEA aims to provide a seamless experience for managing a game store's inventory and customer interactions.




```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── category.py
        |-customer.py
        |-game.py
        |-user.py 
    |
    ├── cli.py
    ├── debug.py
    └── helpers.py
    |- seed.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell

```
```seed Database
python lib/seed.py
```


---

## Generating Your CLI
``` access the menu
 python lib/cli.py
```

heres a sample  of `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    list_games,
    game_by_title,
    game_by_category,
    add_game,
    add_customer,
    customer_buys_game,
    user_login,
    delete_game
)

def main():
    if user_login():
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                list_games()
            elif choice == "2":
                game_by_title()
            elif choice == "3":
                game_by_category()
            elif choice == "4":
                add_game()
            elif choice == "5":
                add_customer()
            elif choice == "6":
                customer_buys_game()
            elif choice == "7":
                delete_game()
            else:
                print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all games")
    print("2. Find game by title")
    print("3. Find games by category")
    print("4. Add a game")
    print("5. Add a customer")
    print("6. Customer buys a game")
    print("7. Delete a game")

if __name__ == "__main__":
    main()


The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def list_games():
    print("Listing all games...")

def game_by_title():
    print("Finding game by title...")

def game_by_category():
    print("Finding games by category...")

def add_game():
    print("Adding a new game...")

def add_customer():
    print("Adding a new customer...")

def customer_buys_game():
    print("Processing customer game purchase...")

def delete_game():
    print("Deleting a game...")

def exit_program():
    print("Goodbye!")
    exit()

```
## Data Models

The data models are located in the lib/models directory. Each model corresponds to a table in the database.

`user.py`
Manages user accounts and handles authentication.

`customer.py`
Tracks customers and their information.

`game.py`
Stores details about games, including title, category, and price.

`purchase.py`
Logs purchases made by customers, linking customers to games.

`category.py`
Contains game categories to classify games.

`__init__.py`
Initializes database connections and constants.








