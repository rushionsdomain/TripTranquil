from triptranquil.session.session import get_session
from triptranquil.models.admin import Admin
from triptranquil.models.product import Product

def admin_menu():
    print("Welcome to the Admin CLI")
    print("1. Add Destination")
    print("2. Manage Bookings")
    print("3. View Reviews")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_destination()
    elif choice == "2":
        manage_bookings()
    elif choice == "3":
        view_reviews()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid option")

def add_destination():
    session = get_session()
    name = input("Enter destination name: ")
    price = input("Enter price: ")

    new_destination = Product(name=name, destination=name, price=price)
    session.add(new_destination)
    session.commit()
    print("Destination added!")
