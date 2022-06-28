"""Contains all the birthday related calculations"""

from datetime import datetime, timedelta
from pprint import pprint

from dateutil.relativedelta import relativedelta

from birthday import Birthday


def calculate_age(birthday: datetime, day: datetime):
    """Calculates the age on day"""
    return relativedelta(birthday, day).years


def is_birthday(birthday: datetime, day: datetime):
    return birthday.day == day.day and birthday.month == day.month


def birthday_in_range(
    birthday: Birthday, date: datetime, offset_past: int, offset_future: int
):
    """
    This returns the full date that is within a range of offset_days from date
    offset will be + or -
    """

    # create a list of all the days from date-offset to date+offset and walk them through
    days = []
    for offset in range(-offset_past, offset_future + 1):
        # print("debug: ", offset)
        offset_date = date + timedelta(days=offset)
        # print(offset_date, offset_date.month, offset_date.day, "?", sep="=")
        if offset_date.month == birthday.month and offset_date.day == birthday.day:
            # print(offset_date, "Matcht")
            return offset_date
    # print("False")
    return


# def date_nearest_to_today(day, month, offset):
#     """This returns the full date plus or minus a number of days to 'day'  """
#     # misschien niet nodig
#     pass
#
# date = datetime(2022,6,26)
# print(birthday_in_range(27,6, date, 0, 0 ))
