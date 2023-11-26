# process_manager.py

import psutil
from prettytable import PrettyTable  # Import the PrettyTable library

def run_process_manager():
    while True:
        print(" Menu for Process Manager")
        print("1. List running processes")
        print("2. Terminate a process")
        print("3. Return to the menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a PrettyTable instance to display the table
            process_table = PrettyTable()
            process_table.field_names = ["PID", "Name"]

            # Get a list of running processes
            processes = list(psutil.process_iter(attrs=['pid', 'name']))

            for process in processes:
                process_table.add_row([process.info['pid'], process.info['name']])

            print("Running Processes:")
            print(process_table)  # Print the table
        elif choice == '2':
            pid = int(input("Enter the PID of the process to terminate: "))
            try:
                process = psutil.Process(pid)
                process.terminate()
                print(f"Process with PID {pid} terminated.")
            except psutil.NoSuchProcess:
                print(f"No process found with PID {pid}.")
            except psutil.AccessDenied:
                print(f"Permission denied to terminate process with PID {pid}.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    run_process_manager()
