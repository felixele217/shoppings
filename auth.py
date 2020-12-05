import sqlite3
import functools
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from db import create_user_table, connect_db, insert_into_user_table


DB = "shopping.db"


def login():
    while True:
        logged_in = False
        username = input("Please enter a username: ")
        password = input("Please enter your password: ")
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
            print("Logged in!")


def register():
    connection = connect_db(DB)
    cursor = connection.cursor()
    username = input("Please enter a username: ")
    password = input("Please enter your password: ")
    cursor.execute("SELECT * FROM user WHERE name=?",(username,))
    row = cursor.fetchone()
    if row is None:
        insert_into_user_table(username, password)
    else:
        print(f"{username} already exists in the database!")
