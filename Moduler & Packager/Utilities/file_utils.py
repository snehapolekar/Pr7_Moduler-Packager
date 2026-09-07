def create_file(filename):
    with open(filename, "w") as file:
        file.write("File created successfully.\n")
    print("File created successfully.")


def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")


def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Content written successfully.")


def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
    print("Content appended successfully.")