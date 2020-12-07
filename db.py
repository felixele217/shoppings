import sqlite3
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from datetime import datetime

DB = "shopping.db"


def connect_db(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    return connection


def create_user_table():
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                        name TEXT NOT NULL,
                        password TEXT NOT NULL);
                        """)
        print("Table user created...")
    else:
        print("There was an error with the database connection!")
    conn.close()


def create_item_table():
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("""CREATE TABLE IF NOT EXISTS item (
                        description TEXT NOT NULL,
                        amount REAL,
                        unit TEXT,
                        added_by TEXT NOT NULL, 
                        date TEXT NOT NULL);
                        """)
        print("Table item created...")
    else:
        print("There was an error with the database connection!")
    conn.close()


def create_shopping_table():
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("""CREATE TABLE IF NOT EXISTS shopping (
                        team TEXT NOT NULL,
                        amount TEXT NOT NULL,
                        date TEXT NOT NULL);
                        """)
        print("Table shopping created...")
    else:
        print("There was an error with the database connection!")
    conn.close()


def insert_into_user_table(name, password):
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("INSERT INTO user VALUES (?, ?)", (name, generate_password_hash(password)))
        conn.commit()
        print(f"{name} successfully added to the DB!")


def insert_into_item_table(description, amount, unit, added_by, date):
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("INSERT INTO item VALUES (?, ?, ?, ?, ?)", (description, amount, unit, added_by, date))
        conn.commit()
        print(f"{description} successfully added to the DB!")


def insert_into_shopping_table(team, amount, date=datetime.now()):
    conn = connect_db(DB)
    cursor = conn.cursor()
    if cursor is not None:
        cursor.execute("INSERT INTO shopping VALUES (?, ?, ?)", (team, amount, date))
        conn.commit()
        print(f"Shopping from {date} successfully added to the DB!")

