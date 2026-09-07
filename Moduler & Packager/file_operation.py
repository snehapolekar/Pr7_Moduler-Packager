def create_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "w") as file:
            pass

        print("File created successfully!")

    except OSError as e:
        print("Error:", e)


def write_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    try:
        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully!")

    except OSError as e:
        print("Error:", e)


def read_from_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("File not found!")

    except OSError as e:
        print("Error:", e)


def append_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    try:
        with open(filename, "a") as file:
            file.write(data)

        print("Data appended successfully!")

    except OSError as e:
        print("Error:", e)


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_to_file()
        elif choice == "3":
            read_from_file()
        elif choice == "4":
            append_to_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")