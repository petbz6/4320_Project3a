from datetime import datetime

def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    print("Please enter the dates for the data you are trying to retrieve: ")
    start_date = get_date("Enter the start date (YYYY-MM-DD): ")
    end_date = get_date("Enter the end date (YYYY-MM-DD): ")

    while end_date < start_date:
        print("End date cannot be before start date.")
        end_date = get_date("Enter the end date (YYYY-MM-DD): ")

    return start_date, end_date
