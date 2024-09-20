# triptranquil/__init__.py

from .session.session import init_db

def create_app():
    """Initialize the application and database."""
    print("Initializing the database...")
    init_db()  # Initialize the database and create default users
