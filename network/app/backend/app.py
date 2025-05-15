from flask import Flask, render_template, jsonify
from flask_cors import CORS
from db import get_connection  # same db.py as before

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
