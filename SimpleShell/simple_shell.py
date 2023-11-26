#simple_shell.py

import subprocess
import os
import shutil
import datetime
import getpass
import glob

simple_shell_banner = """
███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗              ███████╗██╗  ██╗███████╗██╗     ██╗     
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝              ██╔════╝██║  ██║██╔════╝██║     ██║     
███████╗██║██╔████╔██║██████╔╝██║     █████╗      █████╗    ███████╗███████║█████╗  ██║     ██║     
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ╚════╝    ╚════██║██╔══██║██╔══╝  ██║     ██║     
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗              ███████║██║  ██║███████╗███████╗███████╗
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝              ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
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

def run_simple_shell():
    current_directory = os.getcwd()
    command_history = []

    while True:
        command = input(f"SimpleShell ({current_directory})> ")
        command_history.append(command)

        if command.lower() == "exit":
            break
        try:
            if command.lower() == "menu":
                break  # Exit to the menu
            elif command.lower() == "pwd":
                print("\n" + current_directory + "\n")
            elif command.lower().startswith("cd"):
                parts = command.split(" ", 1)
                if len(parts) > 1:
                    new_directory = parts[1].strip('\"')  # Remove double-quotes
                    try:
                        if new_directory == "..":
                            # Go up one level
                            current_directory = os.path.dirname(current_directory)
                        else:
                            # Change to the specified directory
                            os.chdir(os.path.join(current_directory, new_directory))
                            current_directory = os.getcwd()
                        print(f"Changed directory to {current_directory}\n")
                    except FileNotFoundError:
                        print(f"Directory not found: {new_directory}\n")
                else:
                    print("Invalid 'cd' command. Usage: 'cd <directory>' or 'cd ..'\n")
            elif command.lower().startswith("touch "):
                new_file = command[6:]
                try:
                    open(new_file, 'w').close()
                    print(f"Created file: {new_file}\n")
                except Exception as e:
                    print(f"Error creating file: {e}\n")
            elif command.lower().startswith("rm "):
                target = command[3:]
                try:
                    if os.path.isfile(target):
                        os.remove(target)
                        print(f"Removed file: {target}\n")
                    elif os.path.isdir(target):
                        shutil.rmtree(target)
                        print(f"Removed directory: {target}\n")
                    else:
                        print(f"File or directory not found: {target}\n")
                except Exception as e:
                    print(f"Error removing: {e}\n")
            elif command.lower().startswith("cat "):
                target_file = command[4:]
                try:
                    with open(target_file, 'r') as file:
                        contents = file.read()
                        print(contents + "\n")
                except FileNotFoundError:
                    print(f"File not found: {target_file}\n")
            elif command.lower().startswith("echo "):
                message = command[5:]
                print(message + "\n")
            elif command.lower().startswith("mkdir "):
                new_dir = command[6:]
                try:
                    os.mkdir(new_dir)
                    print(f"Created directory: {new_dir}\n")
                except Exception as e:
                    print(f"Error creating directory: {e}\n")
            elif command.lower().startswith("rmdir "):
                empty_dir = command[6:]
                try:
                    os.rmdir(empty_dir)
                    print(f"Removed directory: {empty_dir}\n")
                except Exception as e:
                    print(f"Error removing directory: {e}\n")
            elif command.lower().startswith("cp "):
                source, destination = command[3:].split()
                try:
                    if os.path.isdir(source):
                        shutil.copytree(source, destination)
                        print(f"Copied directory: {source} to {destination}\n")
                    elif os.path.isfile(source):
                        shutil.copy(source, destination)
                        print(f"Copied file: {source} to {destination}\n")
                    else:
                        print(f"Source not found: {source}\n")
                except Exception as e:
                    print(f"Error copying: {e}\n")
            elif command.lower().startswith("mv "):
                source, destination = command[3:].split()
                try:
                    shutil.move(source, destination)
                    print(f"Moved/Renamed: {source} to {destination}\n")
                except Exception as e:
                    print(f"Error moving/renaming: {e}\n")
            elif command.lower().startswith("find "):
                search_path = command[5:]
                matches = glob.glob(search_path)
                print(f"Matching files/directories in '{search_path}':")
                for match in matches:
                    print(match)
                print("\n")
            elif command.lower() == "history":
                print("\nCommand History:")
                for idx, cmd in enumerate(command_history, 1):
                    print(f"{idx}. {cmd}")
                print("\n")
            elif command.lower() == "clear":
                os.system('clear' if os.name == 'posix' else 'cls')
                print(simple_shell_banner)
                print(simple_shell_description)
                from SimpleShell.simple_shell import run_simple_shell
                run_simple_shell()
            elif command.lower() == "date":
                current_date = datetime.datetime.now()
                print("\n" + current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            elif command.lower() == "who":
                username = getpass.getuser()
                print("\n" + username + "\n")
            elif command.lower() == "df":
                df_output = subprocess.run(["df", "-h"], stdout=subprocess.PIPE, text=True)
                print("\n" + df_output.stdout + "\n")
            elif command.lower() == "du":
                du_output = subprocess.run(["du", "-h", "--max-depth=1"], stdout=subprocess.PIPE, text=True)
                print("\n" + du_output.stdout + "\n")
            else:
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:  # Only display errors if there's an error
                    print("\n")
                    print("Output:\n" + result.stdout)
                else:
                    print("Error:\n" + result.stderr)
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    run_simple_shell()
