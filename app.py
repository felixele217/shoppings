# application to track shoppings
# author: felixele217
# TODO added databases and insertions for user item and shopping. now need to add the functionality for
# TODO the several inputs in the menu

import sys
from auth import register, login
from db import create_user_table
from item import items


def start():
    print("Hey there and welcome to the Shopping App!\n")
    logged_in = False
    username = None
    while True:
        l_or_r = input("Press l to login or r to register and q to quit: ")
        print("")
        if l_or_r.lower() == "l":
            username = login()
        elif l_or_r.lower() == "r":
            register()
        elif l_or_r.lower() == "q":
            sys.exit()
        else:
            print("Wrong input! Try again...")
        if username is not None:
            break
    return username


def display_user(user):
    return f"({user})"


def display_menu(user):
    print(display_user(user), f"Welcome {user}!")
    print(display_user(user),
          """You have the following options:
- i for the items
- s for the shoppings
- q to logout\n""")

    print(display_user(user), end = " ")
    user_input = input("Please enter the option you want to use: ")
    while True:
        if user_input.lower() == "i":
            items(user)
        if user_input.lower() == "s":
            # shoppings()
            return
        if user_input.lower() == "q":
            print(f"{user} has been logged out...\n")
            return



def main():
    # starting the program with login or register
    while True:
        logged_in_user = start()
        display_menu(logged_in_user)



if __name__ == "__main__":
    main()
