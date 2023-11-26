# file_system_viewer.py
import os

def run_file_system_viewer():
    while True:
        print("Menu for File System Viewer")
        print("1. List files and directories in the current directory")
        print("2. Change current directory")
        print("3. Go back to the parent directory")
        print("4. Return to the menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            current_directory = os.getcwd()
            items = os.listdir(current_directory)
            print("\n")
            print(f"Contents of {current_directory}:")
            for item in items:
                if os.path.isfile(item):
                    print(f"File: {item}")
                elif os.path.isdir(item):
                    print(f"Directory: {item}")
            print("\n")
        elif choice == '2':
            new_directory = input("Enter the path of the directory to change to: ")
            try:
                os.chdir(new_directory)
                print("\n")
                print(f"Changed directory to {os.getcwd()}")
                print("\n")
            except FileNotFoundError:
                print("\n")
                print(f"Directory not found: {new_directory}")
                print("\n")
        elif choice == '3':
            parent_directory = os.path.dirname(os.getcwd())
            os.chdir(parent_directory)
            print("\n")
            print(f"Changed directory to {os.getcwd()}")
            print("\n")
        elif choice == '4':
            break
        else:
            print("\n")
            print("Invalid choice. Please enter a valid option.")
            print("\n")
