import sqlite3
import functools
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from db import create_user_table, connect_db, insert_into_user_table, insert_into_item_table, insert_into_shopping_table
from datetime import datetime
from app import display_user, start, display_menu

DATE = datetime.now()
DB = "shopping.db"


def add_item(user):
    description = input("Please enter a description for the item: ")
    amount = int(input("Please enter a amount for the item (optional): "))
    unit = input("Please enter a unit for the item (optional): ")
    connection = connect_db(DB)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM item WHERE description=?", (description,))
    row = cursor.fetchone()
    if row is None:
        insert_into_item_table(description, amount, unit, user, datetime.now())
    else:
        print(f"{description} already exists in the database...")


def items(user):
    print("\nWelcome in the item section!")
    print(display_user(user), f"Welcome {user}!")
    print(display_user(user),
          """You have the following options:
- a for adding an item
- s for showing all the items
- m for modifying an item
- l to leave the item section\n""")

    user_input = input("Please input what you want to do: ")
    if user_input == "a":
        add_item(user)
    if user_input == "s":
        return
    if user_input == "m":
        return
    if user_input == "l":
        return display_menu(user)


