from triptranquil.session.session import get_session
from triptranquil.models.user import User

def user_menu():
    print("Welcome to the TripTRanquil User CLI")
    print("1. View Destinations")
    print("2. Book Accommodation")
    print("3. Leave a Review")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_destinations()
    elif choice == "2":
        book_accommodation()
    elif choice == "3":
        leave_review()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid option")

def view_destinations():
    session = get_session()
    destinations = session.query(Product).all()
    for destination in destinations:
        print(f"{destination.id}. {destination.name} - {destination.destination}")

# Other methods like book_accommodation() and leave_review() would be added
