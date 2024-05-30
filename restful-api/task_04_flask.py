#!/usr/bin/python3
""""""
from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404
    
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' in data:
        username = data['username']
        users[username] = data
        return jsonify({"message": "User added", "user": data})
    else:
        return "Missing username in request", 400

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)