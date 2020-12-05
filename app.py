# application to track shoppings
# author: felixele217
# TODO add options to register and login and modify the methods to see if a user is already logged in and stuff

from auth import register, login
from db import create_user_table

create_user_table()
login()