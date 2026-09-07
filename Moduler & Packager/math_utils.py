import math


def factorial():
    try:
        n = int(input("Enter a number: "))

        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return

        print("Factorial:", math.factorial(n))

    except ValueError:
        print("Invalid input!")


def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** time
        interest = amount - principal

        print("Compound Interest:", round(interest, 2))
        print("Total Amount:", round(amount, 2))

    except ValueError:
        print("Invalid input!")


def trigonometric_calculations():
    try:
        angle = float(input("Enter angle in degrees: "))

        radians = math.radians(angle)

        print("Sin:", round(math.sin(radians), 4))
        print("Cos:", round(math.cos(radians), 4))
        print("Tan:", round(math.tan(radians), 4))

    except ValueError:
        print("Invalid input!")


def area_of_shapes():
    print("\nArea of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            print("Area of Circle:", round(math.pi * radius ** 2, 2))

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print("Area of Rectangle:", length * width)

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area of Triangle:", 0.5 * base * height)

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input!")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            area_of_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")