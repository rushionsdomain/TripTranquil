# app.py

from triptranquil.cli.user_cli import user_menu
from triptranquil.cli.admin_cli import admin_menu
from triptranquil.session.session import init_db, create_default_users
from triptranquil.cli.user_cli import user_login

def main():
    # Initialize the database
    print("Initializing the database...")
    init_db()  # Creates all tables in the database if they don't exist

    print("Welcome to TripTranquil!")

    while True:
        print("\n1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            role, logged_in_user = user_login()  # Get role and user after login
            if logged_in_user:
                # Direct to user or admin menu based on role
                if role == 'admin':
                    admin_menu(logged_in_user)
                else:
                    user_menu(logged_in_user)
            else:
                print("Login failed. Please try again.")
        elif choice == '2':
            print("Exiting TripTranquil...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
