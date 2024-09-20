from triptranquil.session.session import get_session
from triptranquil.models.admin import Admin

def admin_menu():
    print("\nAdmin Menu")
    while True:
        print("1. View Admins")
        print("2. Create Admin")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_admins()
        elif choice == '2':
            create_admin()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

def view_admins():
    session = get_session()
    admins = session.query(Admin).all()
    if admins:
        for admin in admins:
            print(f"ID: {admin.id}, Username: {admin.username}, Email: {admin.email}")
    else:
        print("No admins found.")

def create_admin():
    session = get_session()
    username = input("Enter username: ")
    email = input("Enter email: ")

    new_admin = Admin(username=username, email=email)
    session.add(new_admin)
    session.commit()

    print(f"Admin {username} created successfully!")
