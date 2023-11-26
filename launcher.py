# program_launcher.py

import os
import subprocess

programs = {
    1: "Simple Shell",
    2: "Process Manager",
    3: "Memory Allocator",
    4: "File System Viewer",
    5: "Calculator",
}

# Empty banners
menu_banner = """
 ██████╗ ███╗   ███╗███╗   ██╗██╗     ██████╗ ███████╗
██╔═══██╗████╗ ████║████╗  ██║██║    ██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██╔██╗ ██║██║    ██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║╚██╗██║██║    ██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║    ╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝     ╚═════╝ ╚══════╝
"""

simple_shell_banner = """
███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗              ███████╗██╗  ██╗███████╗██╗     ██╗     
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝              ██╔════╝██║  ██║██╔════╝██║     ██║     
███████╗██║██╔████╔██║██████╔╝██║     █████╗      █████╗    ███████╗███████║█████╗  ██║     ██║     
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ╚════╝    ╚════██║██╔══██║██╔══╝  ██║     ██║     
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗              ███████║██║  ██║███████╗███████╗███████╗
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝              ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
"""

process_manager_banner = """
██████╗ ██████╗  ██████╗  ██████╗███████╗███████╗███████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║██║     █████╗  ███████╗███████╗██║   ██║██████╔╝    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║╚════██║██║   ██║██╔══██╗    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝╚██████╗███████╗███████║███████║╚██████╔╝██║  ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

memory_allocator_banner = """
███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗     █████╗ ██╗     ██╗      ██████╗  ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔══██╗██║     ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝ ╚████╔╝     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗  ╚██╔╝      ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║   ██║       ██║  ██║███████╗███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

file_system_viewer_banner = """
███████╗██╗██╗     ███████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗    ██╗   ██╗██╗███████╗██╗    ██╗███████╗██████╗ 
██╔════╝██║██║     ██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║    ██║   ██║██║██╔════╝██║    ██║██╔════╝██╔══██╗
█████╗  ██║██║     █████╗      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║    ██║   ██║██║█████╗  ██║ █╗ ██║█████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║     ╚████╔╝ ██║███████╗╚███╔███╔╝███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
"""

calculator_banner = """
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

# Descriptions for each program
menu_description ="""
The Program Launcher is the main entry point to the OMNI OS operating system. It provides a user-friendly menu to access various built-in programs and utilities. Users can choose from a range of tools,each designed for specific tasks
The launcher serves as the central hub for program execution.

Features:
- Choose from a variety of programs, each tailored for different purposes.
- Access essential operating system functionalities, including a simple shell, process manager, memory allocator, file system viewer, and a basic calculator.
- Seamless navigation: Select a program, run it, and return to the main menu with ease.

Usage:
- Upon launching the Program Launcher, you are presented with a menu that lists available programs.
- Enter the number corresponding to the program you want to run.
- The launcher will execute the chosen program, and you can interact with it as needed.
- To exit the operating system, simply enter '0' or choose the '0. Exit' option from the menu.

Program Descriptions:
1. Simple Shell: A versatile command-line interface with file and directory management, command execution, and more. Use the 'menu' command to return to the launcher.
2. Process Manager: View and manage running processes, terminate processes, and maintain system organization.
3. Memory Allocator: Simulate memory allocation and deallocation, providing a visual representation of memory usage.
4. File System Viewer: Explore and navigate your computer's file system, listing files and directories efficiently.
5. Calculator: A basic command-line calculator for performing arithmetic operations on two numbers.

The Program Launcher simplifies program access within OMNI OS, making it a convenient and user-friendly operating environment.
"""


simple_shell_description = """
The Simple Shell is a command-line interface that allows you to perform various tasks, including navigating directories,
creating and editing files, and running commands. Use the 'menu' command to return to the main menu.

this shell is capable of using commands :-
pwd: Displays the current working directory.
cd <directory>             : Changes the current directory to the specified one. You can navigate to subdirectories or use cd .. to move up one level.
touch <filename>           : Creates a new empty file with the given name.
rm <target>                : Removes a file or directory specified by <target>. This command can delete both files and directories.
cat <filename>             : Reads and displays the contents of a text file specified by <filename>.
echo <message>             : Prints the provided message to the console.
mkdir <directory>          : Creates a new directory with the given name.
rmdir <directory>          : Removes an empty directory.
cp <source> <destination>  : Copies a file or directory from <source> to <destination>. It can copy individual files or entire directories.
mv <source> <destination>  : Moves or renames a file or directory from <source> to <destination.
find <path>                : Searches for files and directories matching a specified pattern within the provided path.
history                    : Displays a history of all previously entered commands.
clear                      : Clears the terminal screen to provide a clean workspace.
date                       : Shows the current date and time.
who                        : Displays the username of the current user.
"""

process_manager_description ="""
This Process Manager is a utility that allows users to view and manage running processes on their system. It provides a simple and intuitive interface for monitoring and controlling processes efficiently.

Features:
1. List Running Processes:
   - View a table of currently active processes, including their Process ID (PID) and names.

2. Terminate a Process:
   - Terminate a running process by entering its PID. The program will attempt to gracefully stop the process.

3. Return to the Menu:
   - Easily navigate between options and return to the main menu for a seamless user experience.

Usage:
- To list running processes, choose option '1'. You'll see a table with process details.
- To terminate a process, select option '2', enter the PID when prompted, and the program will attempt to stop it.
- Return to the menu at any time by selecting option '3'.

Note:
- Terminating processes requires the necessary permissions. In some cases, you may encounter "Permission denied" errors if you try to terminate specific processes.

This Process Manager simplifies the process monitoring and management tasks, making it a valuable tool for users who need to keep their system organized and efficient.
"""


memory_allocator_description = """
The Memory Allocator is a command-line utility that simulates memory allocation and deallocation. It is designed to demonstrate memory management principles and visually represent the allocation status.

Features:
1. Allocate Memory:
   - Reserve a specified amount of memory. The program displays the allocated blocks and available free memory.

2. Deallocate Memory:
   - Release a portion of previously allocated memory. The program updates the memory status accordingly.

3. View Memory Allocation:
   - Observe the memory allocation status as a visual representation of allocated and free memory blocks.

4. Return to the Menu:
   - Easily navigate between options and return to the main menu for a seamless user experience.

Usage:
- Upon launching the program, specify the total memory size.
- Choose from the available options:
   - Allocate memory (option '1').
   - Deallocate memory (option '2').
   - View memory allocation (option '3').
   - Return to the menu (option '4').

Memory Allocation Visualization:
- The program visually represents allocated memory with '#' symbols.
- It displays the percentage of memory allocation.

This Memory Allocator is a valuable tool for understanding memory management concepts. It provides a hands-on experience with memory allocation and visualization, making it a useful learning resource.
"""


file_system_viewer_description ="""
The File System Viewer is a command-line utility that allows you to explore the contents of your computer's file system. It offers a range of features to navigate and view files and directories efficiently.

Features:
1. List Files and Directories:
   - View the files and directories in the current directory.
   - Get a detailed list including file and directory names.

2. Change Current Directory:
   - Navigate to a different directory by specifying its path.
   - Effortlessly switch between directories to explore your file system.

3. Go Back to the Parent Directory:
   - Easily move back to the parent directory to navigate upwards in the file hierarchy.

4. Return to the Menu:
   - Return to the main menu to access different options or exit the program.

Usage:
- When you launch the program, you'll be presented with a menu.
- Select an option from the menu to perform the desired action:
   - List files and directories (option '1').
   - Change the current directory (option '2').
   - Go back to the parent directory (option '3').
   - Return to the menu (option '4').

The File System Viewer provides a convenient way to explore your computer's file system and manage files and directories. It's a practical tool for users who need to navigate their file systems efficiently.
"""


calculator_description ="""
The Calculator is a simple command-line utility that allows you to perform basic arithmetic operations on two numbers. It provides a user-friendly interface for quick calculations.

Features:
1. Addition:
   - Add two numbers to obtain the sum.
   - Enter two numbers, and the calculator will display the result.

2. Subtraction:
   - Subtract the second number from the first.
   - Input both numbers to see the difference.

3. Multiplication:
   - Multiply two numbers to get the product.
   - Provide the numbers, and the calculator will show the outcome.

4. Division:
   - Divide the first number by the second.
   - Enter both numbers for division, and the result will be displayed.

5. Return to the Menu:
   - Return to the main menu to choose a different operation or exit the calculator.

Usage:
- Upon launching the program, you'll be greeted with a menu offering various arithmetic operations.
- Select an option from the menu to perform the desired calculation:
   - Addition (option '1').
   - Subtraction (option '2').
   - Multiplication (option '3').
   - Division (option '4').
   - Return to the menu (option '5').

The Calculator is a handy tool for performing basic calculations without the need for a graphical calculator application. It's suitable for users who want a quick and straightforward way to perform arithmetic operations on two numbers.
"""


def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(menu_banner)
    print(menu_description)
    print("MENU:")
    for key, value in programs.items():
        print(f"{key}. {value}")

def launch_program(program_choice):
    if program_choice in programs:
        if program_choice == 1:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(simple_shell_banner)
            print(simple_shell_description)
            from SimpleShell.simple_shell import run_simple_shell
            run_simple_shell()
            show_menu()
        elif program_choice == 2:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(process_manager_banner)
            print(process_manager_description)
            from ProcessManager.process_manager import run_process_manager
            run_process_manager()
            show_menu()
        elif program_choice == 3:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(memory_allocator_banner)
            print(memory_allocator_description)
            from MemoryAllocator.memory_allocator import run_memory_allocator
            run_memory_allocator()
            show_menu()
        elif program_choice == 4:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(file_system_viewer_banner)
            print(file_system_viewer_description)
            from FileSystemViewer.file_system_viewer import run_file_system_viewer
            run_file_system_viewer()
            show_menu()
        elif program_choice == 5:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(calculator_banner)
            print(calculator_description)
            from Calculator.calculator import run_calculator
            run_calculator()
            show_menu()
    else:
        print("Invalid choice. Please select a valid program.")

if __name__ == "__main__":
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (0 to exit): "))
            if choice == 0:
                print("Goodbye!")
                break
            launch_program(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
