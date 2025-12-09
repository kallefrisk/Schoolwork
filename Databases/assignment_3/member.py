from Database import database


# Function for adding a user to the system

def add_user(db:database):          # input all information with correct corresponding conditions. (E.g. no numbers in name or no letters in phone number etc.)
    fname = is_letters("\nEnter first name:  ", "Only letters in the name!")
    lname = is_letters("\nEnter last name:  ", "Only letters in the name")
    street = input("\nEnter street address:  ")
    city = is_letters("\nEnter city:  ", "Only letters in city name!")
    state = is_letters("\nEnter state:  ", "Only letters in state name!")
    zip = is_numbers("\nEnter zip:  ", "Only numbers in zip code!")
    phone = is_numbers("\nEnter phonenumber:  ", "only nembers in phone number!")
    email = check_email(db)
    password = input("\nEnter new password:  ")
    try:
        insert_query = f""" INSERT INTO members (fname, lname, address, city, state, zip, phone, email, password)
        VALUES ("{fname}", "{lname}", "{street}", "{city}", "{state}", "{zip}", "{phone}", "{email}", "{password}") """
        db.execute_with_commit(insert_query)        # Try to add user
        print("\nADDING user has succeeded")
    except Exception as e:
        print("\nADDING user has failed!")          # Print out error message should it not work
        print(e)


# Function for checking if an email is valid(in this case it only requires an @ to be present)

def check_email(db:database):
    email = None
    while email is None:
        email = input("\nEnter e-mail:  ")      # input an email
        if "@" not in [c for c in email]:       # check if "@" in email                 "my criteria to pass as an email"
            print(f"{email} is not a valid email!")
            email = None
        email_query = """SELECT email FROM members"""
        emails_tuples = db.execute_with_fetchall(email_query)   # Fetch existing emails
        emails = [c[0] for c in emails_tuples]
        if email in emails:                                     # Check if email already exists
            print("\nEmail already in use!\n")                  # Print out error message
            email = None
    return email                                                # Return acceptable email


# Function for confirming if a user and password match
# and returning the userid for coming functions

def member_login(db:database):
    email = None
    password = None
    while email is None:
        email = input("Enter e-mail or\ntype 'exit' to\nreturn to main menu:  ")        # Input email
        if email == "exit":                                                             # Extra functionality to get out of login screen without re-entering server user and password
            email = None
            return email
        else:
            email_query = """SELECT email FROM members;"""
            emails = db.execute_with_fetchall(email_query)                              # Fetch all emails
            members = [c[0] for c in emails]
            if email in members:                                                        # Check if email exists
                continue
            else:
                print("User not found!")
                email = None
    while password is None:
        password = (email, input("Enter password:  "))                                  # Input password for the email
        password_query = f"""SELECT email, password FROM members WHERE email = "{email}";"""
        links = db.execute_with_fetchall(password_query)                                # Fetch password for the email
        if password in links:                                                           # If passwords match you log in
            print("Login SUCCESSFULL!")
            userid_query = f"""SELECT userid FROM members WHERE email = "{email}";"""
            userid = db.execute_with_fetchall(userid_query)                             # Fetch userid for the email
        else:
            print("Incorrect password!")
            password = None
    return (userid[0])[0]                                                               # Return the userid for later functions


# Function to check if input is letters only

def is_letters(statement, correctment):
    output = None
    while output is None:
        output = input(statement)
        for i in output:
            if i.isalpha():
                continue
            else:
                print(correctment)
                output = None
                break
    return output


# Function to check if input is numbers only

def is_numbers(statement, correctment):
    output = None
    while output is None:
        output = input(statement)
        for i in output:
            if not i.isalpha():
                continue
            else:
                print(correctment)
                output = None
                break
    return output
