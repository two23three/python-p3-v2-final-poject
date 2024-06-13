# lib/cli.py

from helpers import (
    exit_program,
    list_games,
    game_by_title,
    game_by_category,
    add_game,
    add_customer,
    customer_buys_game,
    delete_game,
    user_login,
    update_game

    
)


def main():
    logged_in = False
    while not logged_in:
        logged_in=user_login()
   
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
        elif choice == "8":
            update_game()   
            
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all games")
    print("2. Get game by title")
    print("3. Get games by category")
    print("4. Add new game")
    print("5. add customer")
    print("6. customer purchase game")
    print("7. Delete game")
    print("8. Update game")
if __name__ == "__main__":
    main()
