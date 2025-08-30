from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
an = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskan"
)

cursor = an.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return jsonify(rows)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
