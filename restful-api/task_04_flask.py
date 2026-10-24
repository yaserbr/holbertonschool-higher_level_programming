#!/usr/bin/python3
"""A simple RESTful API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return the welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user information by username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API."""
    user_data = request.get_json(silent=True)

    if not isinstance(user_data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
