from Database import database
from mysql.connector import connect
from getpass import getpass
import main_menu as m
import member as mem
import shop as s


# Main menu function

def menu(db:database):
    while True:
        m.print_header("WELCOME TO THE ONLINE BOOKSTORE!", None)                                # Print header
        m.print_options(["Member Login", "New Member Registration", "Quit"])                    # print option
        choice = m.check_choice(["Member Login", "New Member Registration", "Quit"])            # Check if choice is valid
        match choice:
            case 0:
                userid = mem.member_login(db)               # Choice for login and save the userid for coming functions
                if userid is not None:
                    s.shop(db, userid)
            case 1:
                mem.add_user(db)                            # Choice for adding a new user
            case 2:
                exit()                                      # Exit program


# Function for checking if successfull login

def check_credentials(username, password):
    try:
        connect(host="localhost", user=username, password=password, database="book_store")
        return True
    except:
        return False


# Code requesting user input for login to database

valid_connection = False
while not valid_connection:
    username = input("Enter your SQL server Username:")
    password = getpass("Enter your SQL server Password:")

    if check_credentials(username, password):
        valid_connection = True
    else:
        print("Incorrect username or password! Please make sure the username and password are correct!")

db = database(username, password)


# Excecute program

menu(db)
