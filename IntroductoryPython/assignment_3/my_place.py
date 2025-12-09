import os


# Function counting directories in "path"
def count_directories(path):
    current = os.scandir()
    directory = 0
    for c in current:
        if c.is_dir:
            directory += 1
    return directory


# Function counting files in "path"
def count_files(path):
    current = os.scandir()
    file = 0
    for c in current:
        if c.is_file():
            file += 1
    return file


path = os.getcwd()

# Print results
print(f"I am currently at {path}.")
print(f"Below me I have {count_directories(path)} directories/folders.")
print(f"This folder contains {count_files(path)} files.")
