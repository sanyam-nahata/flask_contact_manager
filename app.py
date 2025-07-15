# app.py
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id;")
    contacts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        name  = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        conn = get_db_connection()
        cur  = conn.cursor()
        cur.execute(
            "INSERT INTO contacts (name, email, phone) VALUES (%s,%s,%s);",
            (name, email, phone)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE id = %s;", (id,))
    contact = cur.fetchone()
    if request.method == "POST":
        name  = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cur.execute(
            "UPDATE contacts SET name=%s,email=%s,phone=%s WHERE id=%s;",
            (name, email, phone, id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    cur.close()
    conn.close()
    return render_template("edit.html", contact=contact)

@app.route("/delete/<int:id>", methods=("POST",))
def delete(id):
    conn = get_db_connection()
    cur  = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

