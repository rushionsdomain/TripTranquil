TripTranquil CLI Application
============================

Welcome to the **TripTranquil** CLI Application! This application allows administrators to manage users and trips in a user-friendly command-line interface. Built with Python and SQLAlchemy, it provides a streamlined experience for managing travel-related data.

Features
--------

*   **User Management**: View all users in the system, including their roles (admin or regular user).
*   **Trip Management**: Admins can view, create, edit, and delete trips. Each trip includes:
    *   **Destination**: Where the trip is heading.
    *   **Start and End Dates**: Duration of the trip.
    *   **Duration**: How long the trip lasts.
    *   **Price**: Cost of the trip, formatted for easy readability.
*   **CLI Navigation**: Intuitive menu-driven interface for easy access to various functionalities.

Tools Used
----------

*   **Python**: The primary programming language used to build the application.
*   **SQLAlchemy**: ORM (Object-Relational Mapping) tool used to interact with the SQLite database.
*   **SQLite**: The lightweight database used for storing user and trip information.
*   **Regex**: Utilized for parsing and cleaning user inputs, particularly for price formatting.
*   **Datetime**: For handling and formatting dates associated with trips.

Getting Started
---------------

Follow these steps to set up and run the TripTranquil CLI application locally:

### Cloning the Project

1.  Open your terminal.
    
2.  Clone the repository using the following command:
    
    ```bash
    git clone https://github.com/rushionsdomain/TripTranquil.git
    ```
    
3.  Navigate into the project directory:
    
    ```bash
    
    cd TripTranquil
    ```
    

### Remove the Existing Database

If you need to start fresh, you can remove the existing database file with the following command:

```bash

rm triptranquil.db
```

### Run the Application

To run the application, use one of the following commands depending on your Python installation:

```bash
python app.py
```

or

```bash
python3 app.py
```

### Enjoy the CLI Application

Once the application is running, follow the on-screen prompts to navigate through the user and trip management functionalities.

Live Recording
--------------

Check out the live recording of the TripTranquil CLI application in action [here](insert-link-to-live-recording).

Conclusion
----------

The TripTranquil CLI application serves as an efficient tool for managing travel-related data, making it easy for administrators to keep track of users and trips. We hope you enjoy using this application!
