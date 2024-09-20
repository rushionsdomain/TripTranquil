from triptranquil.session.session import get_session
from triptranquil.models.user import User
from triptranquil.models.trip import Trip
import re
from datetime import datetime

session = get_session()

def view_all_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Admin: {user.is_admin}")

def view_all_trips():
    trips = session.query(Trip).all()
    for trip in trips:
        print(f"ID: {trip.id}, Destination: {trip.destination}, Dates: {trip.start_date} to {trip.end_date}, Duration: {trip.duration}, Price: ${trip.price:,.2f}")

def create_trip():
    destination = input("Enter destination: ")
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    duration = input("Enter duration: ")
    price_str = input("Enter price (e.g., $1,500): ")

    # Convert string dates to datetime.date objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

    # Clean and convert the price to float
    price = float(re.sub(r'[^\d.]', '', price_str))  # Removes $ and commas

    new_trip = Trip(destination=destination, start_date=start_date, end_date=end_date, duration=duration, price=price)
    session.add(new_trip)
    session.commit()
    print("Trip created successfully.")

def edit_trip():
    trip_id = int(input("Enter the trip ID to edit: "))
    trip = session.query(Trip).get(trip_id)

    if trip:
        trip.destination = input("Enter new destination: ")
        start_date_str = input("Enter new start date (YYYY-MM-DD): ")
        end_date_str = input("Enter new end date (YYYY-MM-DD): ")
        trip.duration = input("Enter new duration: ")
        price_str = input("Enter new price (e.g., $1,500): ")

        # Convert string dates to datetime.date objects
        trip.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        trip.end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        # Clean and convert the price to float
        trip.price = float(re.sub(r'[^\d.]', '', price_str))  # Removes $ and commas

        session.commit()
        print("Trip updated successfully.")
    else:
        print("Trip not found.")

def delete_trip():
    trip_id = int(input("Enter the trip ID to delete: "))
    trip = session.query(Trip).get(trip_id)

    if trip:
        session.delete(trip)
        session.commit()
        print("Trip deleted successfully.")
    else:
        print("Trip not found.")

def manage_trips():
    while True:
        print("\nManaging Trips...")
        print("1. View All Trips")
        print("2. Create Trip")
        print("3. Edit Trip")
        print("4. Delete Trip")
        print("5. Back to Admin Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_trips()
        elif choice == '2':
            create_trip()
        elif choice == '3':
            edit_trip()
        elif choice == '4':
            delete_trip()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(logged_in_admin):
    while True:
        print("\nAdmin Menu")
        print("1. View All Users")
        print("2. Manage Trips")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_users()
        elif choice == '2':
            manage_trips()
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
