""" Forlder creation module using pathlib and useable functions."""

import pathlib
import time

def create_directory_range(start_year, end_year): #Create a function to generate folders for a given range 
    """
    Creates a project sub-directory.
    :param start_year: The starting year of the range.
    :param end_year: The ending year of the range
    """
    for year in range(start_year, end_year + 1):
        pathlib.Path(f"year_{year}").mkdir(exist_ok=True)


def create_directory_from_list(folder_list):  #create folders from a list of names
    """
    Create folders from a list of names.
    :param names: A list of names for the folders.
    """
    for name in folder_list:
        folder_name = name.lower().replace(" ", "_")
        pathlib.Path(folder_name).mkdir(exist_ok=True)

def create_directoy_prefixed(prefix, folder_list): #create prefixed folders by transforming a list of names and adding a prefix
    """
    Create prefixed folders by combining each name with a prefix.
    :param prefix: The prefix to add to each name.
    :param names: A list of names for the folders.
    """
    for name in folder_list:
       folder_name = f"{prefix}{name.lower().replace(' ', '_')}"
       pathlib.Path(folder_name).mkdir(exist_ok=True)

def create_directory_periodically(interval, num_folders): #create folders periodically
    """
    Create folders periodically with a specified interval.
    :param interval: The time interval in seconds between folder creation.
    :param num_folders: The number of folders to create.
    """
    for _ in range(num_folders):
        folder_name = f"Folder_{time.strftime('%Y-%m-%d_%H-%M-%S')}"
        pathlib.Path(folder_name).mkdir(exist_ok=True)
        time.sleep(interval)

def main():
    
    #Function 1: For item in Range
    create_directory_range(2022, 2025)

    #Function 2: For Item in List
    folders = ["Customer", "Open Project", "Closed Projects"]
    create_directory_from_list(folders)

    #Function 3: List Comprehension
    projects = ["Project A", "Project B", "Project C"]
    create_directoy_prefixed("data-", projects)

    #Function 4: While Loop
    create_directory_periodically(5, 3)

if __name__ == '__main__':
    main()
