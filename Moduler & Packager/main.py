import math
import datetime_utils
import math_utils
import random_utils
import file_operation


def explore_module_attributes():
    print("\nExplore Module Attributes:")
    print("1. math")
    print("2. datetime_utils")
    print("3. math_utils")
    print("4. random_utils")
    print("5. file_operations")

    choice = input("Enter your choice: ")

    modules = {
        "1": math,
        "2": datetime_utils,
        "3": math_utils,
        "4": random_utils,
        "5": file_operation
    }

    if choice in modules:
        module = modules[choice]
        print("Available Attributes:")
        print(dir(module))
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n" + "=" * 30)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 30)

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("=" * 30)

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_utils.datetime_menu()

        elif choice == "2":
            math_utils.math_menu()

        elif choice == "3":
            random_utils.random_menu()

        elif choice == "4":
            import uuid
            print("\nGenerate Unique Identifiers:")
            print("Generated UUID:", uuid.uuid4())

        elif choice == "5":
            file_operation.file_menu()

        elif choice == "6":
            explore_module_attributes()

        elif choice == "7":
            print("\n" + "=" * 30)
            print("Thank you for using the Multi-Utility Toolkit!")
            print("=" * 30)
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
