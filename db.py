import sqlite3
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

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
