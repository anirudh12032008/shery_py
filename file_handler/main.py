from pathlib import Path
import os


def create_folder():
    name = input("tell your new folder name")
    path = Path(name)
    path.mkdir()
    print(f"successfully created a folder named {name}")


def list_files_and_folder():
    path = Path('')
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i + 1} : {items}")


def update_folder():
    try:
        list_files_and_folder()
        old_name = input("which folder you want to update")
        path = Path(old_name)
        if path.exists() and path.is_dir():
            name = input("tell your new name")
            new_path = Path(name)
            path.rename(new_path)
            print("name changed successfully")
        else:
            print(f"no folder name {old_name} exists try again")
    except Exception as e:
        print(f"An error occured {e} try again")


def delete_folder():
    try:

        list_files_and_folder()
        name = input("tell what to delete")
        path = Path(name)
        if path.exists() and path.is_dir():
            path.rmdir()
        else:
            print(f"name {name} doesn't exist")
    except Exception as e:
        print(f"an error occured {e} please try again")


def updatefile():
    try:
        list_files_and_folder()
        name = input('file name')
        path = Path(name)
        if path.exists() and path.is_file():
            print('operations \n 1. rename \n 2. append content \n 3. overwrite content')
            choice = int(input('tell the operation'))
            if choice == 1:
                newname = input('new name with extension')
                newpath = Path(newname)
                if not newpath.exists():
                    path.rename(newpath)
                    print(f'file {name} renamed to {newname}')
                else:
                    print('file already exists of this name')
            elif choice == 2:
                with open(name, 'a') as file:
                    data = input('please tell the content to append')
                    file.write(' ' + data)
                print('appended successfully')
            elif choice == 3:
                with open(name, 'w') as file:
                    data = input('please tell the content to overwrite')
                    file.write(' ' + data)
                print('overwritten successfully')
    except Exception as e:
        print(e)

while True:
    print("press 1 for creating a folder")
    print("press 2 for read a folder")
    print("press 3 for updating a folder")
    print("press 4 for deleating a folder")
    print("press 5 for creating a file")
    print("press 6 for updating a file")
    print("press 7 for deleting a file")
    print("press 8 for reading a file")
    print("press 0 for exiting the application")
    z = input("tell what you want to do")

    if z == "1":
        create_folder()

    elif z == "2":
        list_files_and_folder()

    elif z == "3":
        update_folder()

    elif z == "4":
        delete_folder()
        
    elif z == "6":
        updatefile()
