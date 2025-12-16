# Header creation function

def print_header(title, undertitle):
    dash = "-"
    plus = "+"
    line = "|"
    space = " "
    size = 100
    for i in range(5):
        if i == 0 or i == 4:
            print(plus, dash*(size-2), plus)
        elif i == 1 or i == 3:
            print(line, space*(size-2), line)
        else:

            # Code to center even and uneven length titles and undertitles in header

            if undertitle is None:
                if len(title) % 2 == 0:
                    print(line, space*(((size-2)//2-(len(title)//2))-1), title, space*(((size-2)//2-(len(title)//2))-1), line)
                else:
                    print(line, space*(((size-2)//2-((len(title)+1)//2))-1), title, space*((((size-2)//2-((len(title)+1)//2))-1)+1), line)
            else:
                if len(title) % 2 == 0 and len(undertitle) % 2 == 0:
                    print(line, space*(((size-2)//2-(len(title)//2))-1), title, space*(((size-2)//2-(len(title)//2))-1), line)
                    print(line, space*(((size-2)//2-(len(undertitle)//2))-1), undertitle, space*(((size-2)//2-(len(undertitle)//2))-1), line)
                elif len(title) % 2 == 0 and len(undertitle) % 2 == 1:
                    print(line, space*(((size-2)//2-(len(title)//2))-1), title, space*(((size-2)//2-(len(title)//2))-1), line)
                    print(line, space*(((size-2)//2-((len(undertitle)+1)//2))-1), undertitle, space*((((size-2)//2-((len(undertitle)+1)//2))-1)+1), line)
                elif len(title) % 2 == 1 and len(undertitle) % 2 == 0:
                    print(line, space*(((size-2)//2-((len(title)+1)//2))-1), title, space*((((size-2)//2-((len(title)+1)//2))-1)+1), line)
                    print(line, space*(((size-2)//2-(len(undertitle)//2))-1), undertitle, space*(((size-2)//2-(len(undertitle)//2))-1), line)
                else:
                    print(line, space*(((size-2)//2-((len(title)+1)//2))-1), title, space*((((size-2)//2-((len(title)+1)//2))-1)+1), line)
                    print(line, space*(((size-2)//2-((len(undertitle)+1)//2))-1), undertitle, space*((((size-2)//2-((len(undertitle)+1)//2))-1)+1), line)


# Function to print out a list of options

def print_options(options):
    for i in range(len(options)):
        print()
        print("\t\t\t\t\t", i+1, options[i])


# Function to check if choice is a valid number

def check_choice(options):
    selectedOption = None
    while selectedOption is None:
        choice = input("Type in your choice:  ")
        try:
            selectedOption = int(choice)
            if selectedOption in [n for n in range(1, len(options)+1)]:
                return (selectedOption-1)
            else:
                selectedOption = None
                print("Your choice needs to be one of the options!")
        except Exception:
            selectedOption = None
            print("Your choice needs to be a number!")


# Function for printing a specific add/remove statement

def print_add(statement, title):
    print("-"*150)
    print(f"{statement} \'{title}\' to cart")
    print("-"*150)
