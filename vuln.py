import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.get("/user")
def user():
    name = request.args.get("name", "")
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")  # SQLi
    return str(cur.fetchall())
