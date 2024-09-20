from triptranquil.session.session import get_session
from triptranquil.models.user import User

def user_menu():
    print("\nUser Menu")
    while True:
        print("1. View Users")
        print("2. Create User")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_users()
        elif choice == '2':
            create_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

def view_users():
    session = get_session()
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")

def create_user():
    session = get_session()
    username = input("Enter username: ")
    email = input("Enter email: ")

    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()

    print(f"User {username} created successfully!")
