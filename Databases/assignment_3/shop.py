from Database import database
import main_menu as menu
import checkout as ch


# Main shop function

def shop(db:database, userid):
    while True:                     # Print out the shop menu with options
        menu.print_header("WELCOME TO THE ONLINE BOOKSTORE!", "Member Menu")
        menu.print_options(["Browse by Subject", "Check out", "Logout"])
        choice = menu.check_choice(["Browse by Subject", "Check out", "Logout"])
        match choice:               # Proceed depending on choice
            case 0:
                subjects(db, userid)
            case 1:
                ch.checkout(db, userid)
            case 2:
                return              # Return to main menu


# Function for printing and choosing the different subjects(genre)

def subjects(db:database, userid):
    while True:
        temp = db.execute_with_fetchall("""SELECT DISTINCT subject FROM book_store.books;""")
        subjectslist = [c[0] for c in temp] + ["Exit"]      # Fetch all different subjects from
        menu.print_options(subjectslist)                    # database and print them out
        choice = menu.check_choice(subjectslist)            # to then proceed based on input
        browse(db, subjectslist[choice], userid)
        return


# Function for printing info on the books in the genre and choosing what to do

def browse(db:database, subject, userid):
    offset = 0

    # Fetch number of books within subject
    book_no_query = f"""SELECT COUNT(*) FROM book_store.books WHERE subject = "{subject}";"""
    book_no = db.execute_with_fetchall(book_no_query)
    while True:             # View 2 books at a time from the subject
        book_query = f"""SELECT * FROM book_store.books WHERE subject = "{subject}" LIMIT 2 OFFSET {offset};"""
        books = db.execute_with_fetchall(book_query)
        print((book_no[0])[0], "books available in this Subject")

        for c in books:     # Present information of the current two books
            print()
            print("Author:\t", c[1])
            print("Title:\t", c[2])
            print("ISBN:\t", c[0])
            print("Price:\t", c[3])
            print("Subject:", c[4])
        print("\n\nEnter ISBN to add to Cart or\n"  # Print out options/instructions
                + "n ENTER to browse or\n"
                + "ENTER to go back to menu:")
        n = check_isbn(db, userid)                  # Let function check if input is ISBN
        if n == "":
            return
        elif n == "n" or n == "N":
            offset += 2                             # Display the next two books


# Function interpreting the input for what to happen

def check_isbn(db:database, userid):
    isbn = input()
    isbn_query = """SELECT isbn FROM books;"""      # Fetch all book ISBN's
    isbn_list_tuples = db.execute_with_fetchall(isbn_query)
    isbn_list = [c[0] for c in isbn_list_tuples]
    if isbn in ["", "n", "N"]:
        return isbn
    elif isbn in isbn_list:                         # If input is an ISBN
        add_books(db, isbn, userid)                 # proceed to add_books function
    elif isbn not in ["", "n", "N"]:
        return print("Follow instructions!")


# Function for adding a book to the cart with desired quantity

def add_books(db:database, isbn, userid):
    title_query = f"""SELECT title FROM book_store.books WHERE isbn = "{isbn}";"""
    title = (db.execute_with_fetchall(title_query)[0])[0]   # Fetch title for the book
    print("Add")
    print("-"*100)
    print(title, "\t\tY/N")
    print("-"*100)
    answer = input()                    # Ask if book should be added
    if answer == "N" or answer == "n":
        menu.print_add("Did not add", title)
    elif answer == "Y" or answer == "y":
        qty = None
        while qty is None:
            try:
                qty = int(input("Enter quantity:  "))       # Ask for quantity of books
            except:
                print("Quantity can only be numbers")
        add_query = f"""INSERT INTO cart VALUE ("{userid}", "{isbn}", "{qty}");"""
        cart_query = f"""SELECT userid, book_isbn FROM cart WHERE userid = "{userid}";"""
        cart_list = db.execute_with_fetchall(cart_query)
        if (userid, isbn) not in cart_list:                 # Check if book already exists in cart
            if qty >= 0:                                    # Add book if book does not exist in cart
                db.execute_with_commit(add_query)
                menu.print_add(f"Added {qty}", title)
            elif qty < 0:
                print("No books to remove from cart!")
            else:
                print("Follow instructions!")
        else:                                               # Update cart if book alredy exists in cart
            update_cart_query = f"""UPDATE cart SET qty = qty + {qty} WHERE userid = "{userid}";"""
            db.execute_with_commit(update_cart_query)
            if qty > 0:
                menu.print_add(f"Added {qty} more", title)
            elif qty < 0:
                menu.print_add(f"Removed {-qty}", title)
            else:
                print("Follow instructions!")
