import os

def print_directory_contents(path='/'):
    """
    Print the names of all entries (files and directories)
    in the directory given by `path`.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    # You can change this path to the directory you want to list
    directory_path = input("Enter directory path (or press Enter for current directory): ")
    if not directory_path:
        directory_path = '.'
    print_directory_contents(directory_path)
