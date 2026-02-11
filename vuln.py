import sqlite3
import subprocess
import os
import pickle
import base64


#  SQL Injection
def login(username, password):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Vulnerable query (string concatenation)
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    return cursor.fetchall()


#  Command Injection
def ping(host):
    # Vulnerable use of shell=True
    return subprocess.call("ping -c 1 " + host, shell=True)


#  Unsafe Deserialization
def deserialize(data):
    decoded = base64.b64decode(data)
    obj = pickle.loads(decoded)  # Insecure
    return obj


#  Path Traversal
def read_file(filename):
    filepath = os.path.join("/tmp/", filename)
    with open(filepath, "r") as f:
        return f.read()


#  Code Injection
def calculate(expression):
    return eval(expression)
