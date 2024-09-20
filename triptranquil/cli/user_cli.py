# triptranquil/cli/user_cli.py

from triptranquil.session.session import get_session
from triptranquil.models.user import User
from triptranquil.models.trip import Trip
from triptranquil.models.booking import Booking
from datetime import datetime

session = get_session()

def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    user = session.query(User).filter_by(email=email).first()
    
    if user and user.check_password(password):
        print(f"Welcome {user.username}!")
        
        if user.is_admin:
            return 'admin', user
        else:
            return 'user', user
    else:
        print("Invalid credentials. Please try again.")
        return None, None

def view_trips():
    trips = session.query(Trip).all()
    for trip in trips:
        print(f"ID: {trip.id}, Destination: {trip.destination}, Start: {trip.start_date}, End: {trip.end_date}, Price: {trip.price}")

def search_trips():
    criteria = input("Enter destination or date (YYYY-MM-DD): ")
    trips = session.query(Trip).filter((Trip.destination.ilike(f"%{criteria}%")) | (Trip.start_date == criteria)).all()
    for trip in trips:
        print(f"ID: {trip.id}, Destination: {trip.destination}, Start: {trip.start_date}, End: {trip.end_date}, Price: {trip.price}")

def book_trip(user):
    view_trips()
    trip_id = int(input("Enter the ID of the trip you want to book: "))
    trip = session.query(Trip).get(trip_id)

    if trip:
        new_booking = Booking(user_id=user.id, trip_id=trip.id, booking_date=datetime.now())
        session.add(new_booking)
        session.commit()
        print(f"Trip to {trip.destination} booked successfully!")
    else:
        print("Invalid trip ID. Please try again.")

def view_bookings(user):
    bookings = session.query(Booking).filter_by(user_id=user.id).all()
    for booking in bookings:
        print(f"Trip: {booking.trip.destination}, Date: {booking.booking_date}")

def user_menu(logged_in_user):
    while True:
        print("\n1. View Trips")
        print("2. Search Trips")
        print("3. Book a Trip")
        print("4. View My Bookings")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_trips()
        elif choice == '2':
            search_trips()
        elif choice == '3':
            book_trip(logged_in_user)
        elif choice == '4':
            view_bookings(logged_in_user)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
