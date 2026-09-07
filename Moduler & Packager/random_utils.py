import random
import string


def generate_random_number():
    try:
        start = int(input("Enter minimum number: "))
        end = int(input("Enter maximum number: "))

        if start > end:
            print("Minimum cannot be greater than maximum.")
            return

        print("Random Number:", random.randint(start, end))

    except ValueError:
        print("Invalid input!")


def generate_random_list():
    try:
        size = int(input("Enter list size: "))
        start = int(input("Enter minimum number: "))
        end = int(input("Enter maximum number: "))

        if size < 0 or start > end:
            print("Invalid range or size.")
            return

        numbers = [random.randint(start, end) for _ in range(size)]
        print("Random List:", numbers)

    except ValueError:
        print("Invalid input!")


def create_random_password():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Length must be positive.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        print("Generated Password:", password)

    except ValueError:
        print("Invalid input!")


def generate_random_otp():
    otp = "".join(random.choices(string.digits, k=6))
    print("Generated OTP:", otp)


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            create_random_password()
        elif choice == "4":
            generate_random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")