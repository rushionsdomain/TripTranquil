from triptranquil.session.session import init_db
from triptranquil.cli.user_cli import user_menu
from triptranquil.cli.admin_cli import admin_menu

def main():
    # Initialize the database
    print("Initializing the database...")
    init_db()  # This creates all tables in the database if they don't exist

    print("Welcome to TripTranquil!")
    while True:
        print("\n1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_menu()  # User menu for interacting with user-related options
        elif choice == '2':
            admin_menu()  # Admin menu for admin-related interactions
        elif choice == '3':
            print("Exiting TripTranquil...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()