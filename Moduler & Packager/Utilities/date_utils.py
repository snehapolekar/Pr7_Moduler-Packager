from datetime import datetime


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def format_date(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return date.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid date format!"


def calculate_days(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        return abs((d2 - d1).days)
    except ValueError:
        return "Invalid date format!"