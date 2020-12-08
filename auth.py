import sqlite3
import functools
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from db import create_user_table, connect_db, insert_into_user_table


DB = "shopping.db"


def login():
    print("You can press q to return to login/register functionality.\n")
    logged_in = False
    while not logged_in:
        username = input("[Login] Please enter a username: ")
        if username.lower() == "q":
            print("")
            return logged_in
        password = input("[Login] Please enter your password: ")
        with sqlite3.connect("shopping.db") as db:
            cursor = db.cursor()
        user = cursor.execute("SELECT * from user WHERE name = ?", (username,)).fetchone()
        if user is None:
            print("Incorrect username")
        elif not check_password_hash(user[1], password):
            print("Incorrect password")
        elif check_password_hash(user[1], password):
            logged_in = True

        if logged_in:
            print("[Login] Logged in!\n")
            return username


def register():
    print("You can press q to return to login/register functionality.\n")
    registered = False
    connection = connect_db(DB)
    cursor = connection.cursor()

    while not registered:
        username = input("[Register] Please enter a username: ")
        if username.lower() == "q":
            print("")
            return registered
        cursor.execute("SELECT * FROM user WHERE name=?",(username,))
        row = cursor.fetchone()
        if row is None:
            password = input("[Register] Please enter your password: ")
            if password.isalnum():
                insert_into_user_table(username, password)
                print(f"[Register] {username} successfully registered!")
                registered = True
                return registered
            else:
                print("There were invalid characters in your password...")
        else:
            print(f"{username} already exists in the database!\n")

