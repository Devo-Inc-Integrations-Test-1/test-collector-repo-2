import sqlite3
import os

SECRET_KEY = "hardcoded_secret_key_12345"
DB_PASSWORD = "admin123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection vulnerability - for CodeQL to detect
    query = "SELECT * FROM users WHERE username = '" + username + '"
    cursor.execute(query)
    return cursor.fetchone()

def read_file(path):
    # Path traversal - for CodeQL to detect
    with open("/var/data/" + path) as f:
        return f.read()

def run_command(user_input):
    # Command injection - for CodeQL to detect
    os.system("echo " + user_input)

