# Problem: REST API Development with Flask
# - Description: Build a simple REST API using the Flask framework.
# - Code:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message='Hello, Flask API!')

if __name__ == '__main__':
    app.run(debug=True)

# Problem: Database Interaction with SQLAlchemy
# - Description: Connect Python to a relational database using the SQLAlchemy library.
# - Code:
