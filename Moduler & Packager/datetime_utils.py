from datetime import datetime
import time


def display_current_datetime():
    now = datetime.now()
    print("Current Date and Time:",
          now.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_difference():
    try:
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((d2 - d1).days)

        print("Difference:", difference, "days")

    except ValueError:
        print("Invalid date format!")


def format_custom_date():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        d = datetime.strptime(date, "%Y-%m-%d")

        print("Custom Format:", d.strftime("%d-%m-%Y"))

    except ValueError:
        print("Invalid date format!")


def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()

    input("Press Enter to stop stopwatch...")
    end = time.time()

    print("Elapsed Time:", round(end - start, 2), "seconds")


def countdown_timer():
    try:
        seconds = int(input("Enter countdown seconds: "))

        if seconds < 0:
            print("Enter a positive number.")
            return

        for i in range(seconds, 0, -1):
            print("Time Left:", i, "seconds")
            time.sleep(1)

        print("Time's up!")

    except ValueError:
        print("Invalid input!")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            calculate_difference()
        elif choice == "3":
            format_custom_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")