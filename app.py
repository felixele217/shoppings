# application to track shoppings
# author: felixele217
# TODO after login in display the name of the logged in user on the left and bring him to a menu where he can chose
# TODO further options. commenting code so far

from auth import register, login
from db import create_user_table


def start():
    print("Hey there and welcome to the Shopping App!\n")
    logged_in = False
    username = None
    while True:
        l_or_r = input("Press l to login or r to register: ")
        print("")
        if l_or_r.lower() == "l" and logged_in == False:
            username = login()
        elif l_or_r.lower() == "l" and logged_in == True:
            print("Already logged in!")
        elif l_or_r.lower() == "r":
            register()
        else:
            print("Wrong input! Try again...")
        if username is not None:
            break
    return username


def main():
    # starting the program with login or register
    logged_in_user = start()


if __name__ == "__main__":
    main()




