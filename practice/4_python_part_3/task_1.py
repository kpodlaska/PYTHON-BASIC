"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime, date

"""def calculate_days(from_date: str) -> int:
    format="%d-%m-%Y"
    converted_date=datetime.strftime(from_date,format)
    today = date.today()
    delta = today - converted_date
    return delta.days
    print(f"Data startowa jest{converted_date}")"""

# Function to convert string to datetime
def convert(date_time):

    format = '%d-%m-%Y'# The format
    datetime_str = datetime.strptime(date_time, format)
    start_date=date(datetime_str.year, datetime_str.month,datetime_str.day)


    return start_date

    #return datetime_str
    #print(f"To jest data startowa to {start_date}")




def current_date():
    today = date.today()
    #formatted_today=today.strftime('%d-%m-%Y')
    return today
    #print("Today's date:", today)

def test_current_date():
    assert date.today() == date(2022, 4, 28)


def calculate_days(from_date):
    try:
        s_date=convert(from_date) #start date
        f_date=current_date() #current date aka finish date


        delta = f_date - s_date
        print(f"Pomiędzy datami {s_date} oraz {f_date} (dzisiaj) było {delta.days} dni")
    except ValueError:
        print(f"WrongFormatException dla {from_date} powinno byc dd-mm-yyyy z uzyciem dowolnych ciapkow")


convert("01-03-2020")
current_date()
calculate_days("22-03-2020")
calculate_days("22-03-2024")
calculate_days("2020-03-23")


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
