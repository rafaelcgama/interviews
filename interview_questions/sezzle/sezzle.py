# Requirements / Instructions
#
# Build a Flask API with a GET /users endpoint.
#
# Endpoint behavior:
# - HTTP method: GET
# - Path: /users
# - Always return HTTP status code 200
#
# Data source:
# - Use a mock database function named get_users()
# - get_users() returns a list of dictionaries
# - Each dictionary contains:
#     - id
#     - name
#     - role
#
# Query parameters:
# - Optional query parameter: name
#
# Filtering logic:
# - If the "name" query parameter is provided:
#     - Return only users whose "name" field is exactly equal to the query value
# - If no users match the name:
#     - Return an empty list
# - If "name" is not provided:
#     - Return all users
#
# Response format:
# - JSON array of user objects
# - No error responses required for this endpoint

from flask import Flask, jsonify, request

app = Flask(__name__)

def get_users():
    # Mock database - in the problem solution box you just use the function, the data is given in the background
    return [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"},
        {"id": 3, "name": "Alice", "role": "user"},
    ]

@app.route("/users", methods=["GET"])
def get_users_endpoint():
    name_query = request.args.get("name")

    users = get_users()

    if name_query is not None:
        users = [
            user
            for user in users
            if user.get("name") == name_query
        ]

    return jsonify(users), 200


if __name__ == "__main__":
    app.run(debug=True)