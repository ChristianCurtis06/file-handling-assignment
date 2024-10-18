# Task 1: Directory Inspector
import os

def list_directory_contents(path):
    try:
        dir_list = os.listdir(path)
        print(f"Directory Contents:")
        for file in dir_list:
            print(f" - {file}")
    except FileNotFoundError:
        print("FileNotFoundError: Invalid path. Please try again.")
    except PermissionError:
        print("PermissionError: Invalid directory. Please try again.")

while True:
    path_input = input("Enter the directory path: ")
    list_directory_contents(path_input)

    continue_input = input("Would you like to list the contents of another directory? (yes/no) ").lower()
    if continue_input != "yes":
        break