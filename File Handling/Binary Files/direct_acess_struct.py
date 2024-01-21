"""
Following operations are to be performed using the following code:
1. Create file
2. Insert record
3. Search record
4. Update record
5. Delete record
6. Display all records
"""

import struct

format = "i20sf"
size = struct.calcsize(format)

def create_file():
    with open("file.dat", "wb") as file:
        for i in range(1000):
            file.write(struct.pack(format, 0, " ".encode(), 0.0))
    
    print("File created!")

def insert_record():
    global size, format

    inputId = int(input("Enter id: "))
    inputName = input("Enter name: ")
    inputFee = float(input("Enter fee: "))

    hash = inputId % 1000

    try:
        with open("file.dat", "+rb") as file:
            file.seek(hash * size)
            record = file.read(size)
            id, name, fee = struct.unpack(format, record)
            if id == 0:
                file.seek(-size, 1)
                file.write(struct.pack(format, inputId, inputName.encode(), inputFee))
            else:
                while file.tell() != hash * size:
                    record = file.read(size)
                    id, name, fee = struct.unpack(format, record)
                    if id == 0:
                        file.seek(-size, 1)
                        file.write(struct.pack(format, inputId, inputName.encode(), inputFee))
                        break
                    if file.tell() == size * 1000:
                        file.seek(0)
        print("Added record!")
    except FileNotFoundError:
        print("File not found! Please create the file first.")
        


def search_record():
    global size, format

    inputId = int(input("Enter id: "))

    hash = inputId % 1000

    try:
        with open("file.dat", "rb") as file:
            file.seek(hash * size)
            record = file.read(size)
            id, name, fee = struct.unpack(format, record)
            if id == inputId:
                print("Record found!")
                print(f"ID: {id}\nName: {name.decode()}\nFee: {fee}")
            else:
                while file.tell() != hash * size:
                    record = file.read(size)
                    id, name, fee = struct.unpack(format, record)
                    if id == inputId:
                        print("Record found!")
                        print(f"ID: {id}\nName: {name}\nFee: {fee}")
                        break
                    if file.tell() == size * 1000:
                        file.seek(0)
                else:
                    print("Record not found!")
    except FileNotFoundError:
        print("File not found! Please the create the file first.")

def update_record():
    global size, format

    inputId = int(input("Enter id: "))

    hash = inputId % 1000

    try:
        with open("file.dat", "r+b") as file:
            file.seek(hash * size)
            record = file.read(size)
            id, name, fee = struct.unpack(format, record)
            if id == inputId:
                print("Record found!")
                print(f"ID: {id}\nName: {name.decode()}\nFee: {fee}")
                confirm = input("Do you want to update this record? (y/n): ")
                if confirm.lower() == "y":
                    newName = input("Enter new name: ")
                    newFee = float(input("Enter new fee: "))
                    updatedRecord = struct.pack(format, id, newName.encode(), newFee)
                    file.seek(-size, 1)
                    file.write(updatedRecord)
                    print("Record updated successfully!")
                else:
                    print("Update cancelled.")
            else:
                while file.tell() != hash * size:
                    record = file.read(size)
                    id, name, fee = struct.unpack(format, record)
                    if id == inputId:
                        print("Record found!")
                        print(f"ID: {id}\nName: {name.decode()}\nFee: {fee}")
                        confirm = input("Do you want to update this record? (y/n): ")
                        if confirm.lower() == "y":
                            newName = input("Enter new name: ")
                            newFee = float(input("Enter new fee: "))
                            updatedRecord = struct.pack(format, id, newName.encode(), newFee)
                            file.seek(-size, 1)
                            file.write(updatedRecord)
                            print("Record updated successfully!")
                        else:
                            print("Update cancelled.")
                        break
                    if file.tell() == size * 1000:
                        file.seek(0)
                else:
                    print("Record not found!")
    except FileNotFoundError:
        print("File not found! Please create the file first.")

def delete_record():
    global size, format

    inputId = int(input("Enter id: "))

    hash = inputId % 1000

    try:
        with open("file.dat", "r+b") as file:
            file.seek(hash * size)
            record = file.read(size)
            id, name, fee = struct.unpack(format, record)
            if id == inputId:
                print("Record found!")
                print(f"ID: {id}\nName: {name.decode()}\nFee: {fee}")
                confirm = input("Do you want to delete this record? (y/n): ")
                if confirm.lower() == "y":
                    deletedRecord = struct.pack(format, -1, b"", -1.0)
                    file.seek(-size, 1)
                    file.write(deletedRecord)
                    print("Record deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                while file.tell() != hash * size:
                    record = file.read(size)
                    id, name, fee = struct.unpack(format, record)
                    if id == inputId:
                        print("Record found!")
                        print(f"ID: {id}\nName: {name.decode()}\nFee: {fee}")
                        confirm = input("Do you want to delete this record? (y/n): ")
                        if confirm.lower() == "y":
                            deletedRecord = struct.pack(format, -1, b"", -1.0)
                            file.seek(-size, 1)
                            file.write(deletedRecord)
                            print("Record deleted successfully!")
                        else:
                            print("Deletion cancelled.")
                        break
                    if file.tell() == size * 1000:
                        file.seek(0)
                else:
                    print("Record not found!")
    except FileNotFoundError:
        print("File not found! Please create the file first.")


def display_all():
    global size, format

    try:
        with open("file.dat", "rb") as file:
            while file.tell() != size * 1000:
                record = file.read(size)
                id, name, fee = struct.unpack(format, record)
                print(f"{(file.tell()/size) - 1} >", id, name.decode(), fee)
    except FileNotFoundError:
        print("File not found! Please create the file first.")

# Main program (interactive menu)
while True:
    print("1. Create file")
    print("2. Insert record")
    print("3. Search record")
    print("4. Update record")
    print("5. Delete record")
    print("6. Display all records")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()
    elif choice == 2:
        insert_record()
    elif choice == 3:
        search_record()
    elif choice == 4:
        update_record()
    elif choice == 5:
        delete_record()
    elif choice == 6:
        display_all()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")

print("Program terminated.")
