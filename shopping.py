import sqlite3
import functools
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from db import create_user_table, connect_db, insert_into_user_table
class Shopping():
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date