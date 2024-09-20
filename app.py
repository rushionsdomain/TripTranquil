from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database (you can use SQLite or any other database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User and Admin models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}')"

# Routes for users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

# Routes for admins
@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([{"id": admin.id, "username": admin.username, "email": admin.email} for admin in admins])

@app.route('/admins', methods=['POST'])
def create_admin():
    data = request.json
    new_admin = Admin(username=data['username'], email=data['email'])
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({"message": "Admin created"}), 201

# Run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(debug=True)