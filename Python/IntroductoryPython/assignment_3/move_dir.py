import os


# Function for listing directories
def list_dir(path):
    lst = [c.name for c in os.scandir() if c.is_dir()]
    return lst


# Function for listing files
def list_files(path):
    lst = [c.name for c in os.scandir() if c.is_file()]
    return lst


# Set starting directory
path = os.getcwd()

while True:
    # Print ou the options for every iteration
    print("\n1. List directories \n2. Change directory"
          + "\n3. List files \n4. Quit")
    # Different function depenting on input
    n = input()
    if n == "1":
        print()
        lst = list_dir(path)
        # If directory has no child-directories
        if len(lst) == 0:
            print("Empty")
        else:
            # Display child-directories
            for e in lst:
                print(e)
    elif n == "2":
        # Change working directory by input
        path = os.chdir(input("\nWhat directory?: "))
    elif n == "3":
        print()
        lst = list_files(path)
        # If directory has no files
        if len(lst) == 0:
            print("Empty")
        else:
            # Display files
            for e in lst:
                print(e)
    else:
        exit()
