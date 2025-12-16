from Database import database
from datetime import datetime


# Main checkout function

def checkout(db:database, userid):
    print_order(db, userid)                 # Print the current cart contents
    if not confirm_checkout():              # If no; then return
        return
    else:                                   # If yes; then create invoce
        ono = create_order(db, userid)      # Create order for current cart
        print_invoice(db, userid, ono)      # Print out invoice
        fill_odetails(db, userid, ono)      # Fill in order details
        empty_cart(db, userid)              # Empty user cart for next use
        return


# Function for printing out the current contents of the cart

def print_order(db:database, userid):
    cart_contents_query = f"""SELECT book_isbn FROM cart WHERE userid = "{userid}";"""
    cart_content_tuples = db.execute_with_fetchall(cart_contents_query)
    cart_content = [c[0] for c in cart_content_tuples]      # Fetch current books in cart
    print("Current Cart Contents:")
    total = 0
    for i in range(-1, len(cart_content)):
        if i == -1:                         # Print out info on what the columns are
            print("-"*150)
            print("ISBN\t\tTitle\t\t\t\t\t\t\t\t\t\t\t$/unit\t\tQty\t\tTotal")
        else:
            book_title_query = f"""SELECT title FROM books WHERE isbn = "{cart_content[i]}";"""
            book_title_tuples = db.execute_with_fetchall(book_title_query)  # Fetch book title
            title = (book_title_tuples[0])[0]
            price_query = f"""SELECT price FROM books WHERE isbn = "{cart_content[i]}";"""
            price_tuples = db.execute_with_fetchall(price_query)            # Fetch book price
            price = (price_tuples[0])[0]
            qty_query = f"""SELECT qty FROM cart WHERE book_isbn = "{cart_content[i]}";"""
            qty_tuples = db.execute_with_fetchall(qty_query)                # Fetch number of books in cart
            qty = (qty_tuples[0])[0]
            subtotal_query = f"""SELECT qty*price FROM cart, books WHERE book_isbn = isbn AND userid = "{userid}" AND book_isbn = "{cart_content[i]}";"""
            subtotal_tuples = db.execute_with_fetchall(subtotal_query)      # Fetch price for "x" amount of books
            subtotal = (subtotal_tuples[0])[0]
            print("-"*150)
            checkout_row(cart_content[i], title, price, qty, subtotal)      # Run function to format information into clean rows
            total += subtotal                                               # Add each subtotal to the final price
    print("-"*150)
    print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$", round(total, 2))      # Print out final price


# Function for returning formatted rows of the "Cart" to fit

def checkout_row(isbn, title, price, qty, subtotal):
    if len(title) <= 80:                                # Check title length; Titles under 80 characters use one row
        if len(str(round(price, 1))) > 5:               # If statement for fixing number of "\t" needed to a reasonable degree
            print(isbn, "\t", title, (80-len(title))*" ", "\t", round(price, 1), "\t", qty, "\t\t", round(subtotal, 1))
        else:
            print(isbn, "\t", title, (80-len(title))*" ", "\t", round(price, 1), "\t\t", qty, "\t\t", round(subtotal, 1))
    elif len(title) > 80:
        book_title_1 = ""
        book_title_2 = ""                               # Titles over 80 characters need 2 rows
        for c in range(80):
            book_title_1 += title[c]                    # 1:st part of title
        for c in range(80, len(title)):
            book_title_2 += title[c]                    # 2:nd part of title
        if len(str(round(price, 1))) > 5:               # "If" statement for same reason as line 55
            print(isbn, "\t", book_title_1, "\t", round(price, 1), "\t", qty, "\t\t", round(subtotal, 1))
        else:
            print(isbn, "\t", book_title_1, "\t", round(price, 1), "\t\t", qty, "\t\t", round(subtotal, 1))
        print("\t\t", book_title_2)


# Function for confirming checkout

def confirm_checkout():         # Asks for y(Yes) or n(NO)
    choice = None
    while choice is None:
        choice = input("Proceed to check out (Y/N)?:\t\t")
        if choice in ["Y", "y"]:
            return True
        elif choice in ["N", "n"]:
            return False
        else:
            print("Follow instructions!")
            choice = None


# Function creating an order

def create_order(db:database, userid):
    date = datetime.today().strftime("%y-%m-%d")                # Fetch current date
    address_query = f"""SELECT address, city, zip FROM members WHERE userid = "{userid}";"""
    address_tuples = db.execute_with_fetchall(address_query)    # Fetch user address from database
    shipAddress, shipCity, shipZip = (address_tuples[0])[0], (address_tuples[0])[1], (address_tuples[0])[2]
    create_query = f"""INSERT INTO orders (user_id, created, shipAddress, shipCity, shipZip) VALUES ("{userid}", "{date}", "{shipAddress}", "{shipCity}", "{shipZip}" );"""
    db.execute_with_commit(create_query)                        # Insert userid, date and address into order
    ono_query = f"""SELECT LAST_INSERT_ID();"""
    ono_tuples = db.execute_with_fetchall(ono_query)            # Fetch order number of created order
    return (ono_tuples[0])[0]                                   # for later functions


# Function printing out the invoice to be recieved

def print_invoice(db:database, userid, ono):
    name_query = f"""SELECT fname, lname FROM members WHERE userid = "{userid}";"""
    name_tuples = db.execute_with_fetchall(name_query)          # Fetch the name of the user
    name = (name_tuples[0])[0] + " " + (name_tuples[0])[1]
    address_query = f"""SELECT address, city, zip FROM members WHERE userid = "{userid}";"""
    address_tuples = db.execute_with_fetchall(address_query)    # Fetch the address of the user
    shipAddress, shipCity, shipZip = (address_tuples[0])[0], (address_tuples[0])[1], (address_tuples[0])[2]
    print(f"\n\t\t\t\tInvoice for Order no.{ono}\n")
    print("SHIPPING ADDRESS")                                   # Print out shipping address
    print(f"Name:\t {name}")
    print(f"Address: {shipAddress}\n\t {shipCity}\n\t {shipZip}\n")
    print_order(db, userid)                                     # Print out purchased items with amount and price
    input("Press any button to go back to Main Menu!")          # Await input to return to main menu


# Function to transfer cart contents into orderdetals

def fill_odetails(db:database, userid, ono):
    odetails_query = f"""SELECT isbn, qty, price*qty FROM books, cart WHERE isbn = book_isbn and userid = "{userid}";"""
    order_list = db.execute_with_fetchall(odetails_query)       # Fetch information from cart to be transferred to order detals table
    for c in order_list:
        isbn, qty, amount = c[0], c[1], c[2]
        add_query = f"""INSERT INTO odetails (ono, isbn, qty, amount) VALUES ("{ono}", "{isbn}", "{qty}", "{amount}");"""
        db.execute_with_commit(add_query)                       # Insert information into order details table


# Function to clear cart contents

def empty_cart(db:database, userid):
    empty_query = f"""DELETE FROM cart WHERE userid = "{userid}";"""
    db.execute_with_commit(empty_query)                         # Delete all rows in cart table belonging to the user


'''
# Function to remove cancelled orders

def remove_order(db:database, ono):
    delete_query = f"""DELETE FROM orders WHERE ono = "{ono}";"""
    db.execute_with_commit(delete_query)
'''
