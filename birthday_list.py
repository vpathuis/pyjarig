from datetime import datetime

from birthday import Birthday
from calculations import birthday_in_range


class BirthdayList:
    @property
    def list(self):
        """Assemble the list with relevant birthdays"""
        return self._birthdays

    def near_birthdays(self, date: datetime, past_days: int, future_days: int):
        near_birthdays = []
        for bd in self._birthdays:
            if birthday_in_range(bd, date, past_days, future_days):
                near_birthdays.append(bd)
        return near_birthdays

    def __init__(self, birthdays: list):
        """Accepts a list of birthdays, which is a list of Birthday objects (where the year could be unknown)"""
        self._birthdays = birthdays

    def __repr__(self):
        return f"BirthdayList({self._birthdays})"

    def __str__(self):
        return str(self._birthdays)

    def __getitem__(self, item):
        return self._birthdays[item]


bd1 = Birthday(year=1975, month=12, day=1)
bd2 = Birthday(year=1975, month=12, day=2)
bd3 = Birthday(month=12, day=3)
bdl = [bd1, bd2, bd3]
today = datetime(2022, 12, 4)

bla = BirthdayList(bdl)
print(repr(bla))
print("full list:", bla)
print("near birthdays:", bla.near_birthdays(today, 2, 2))
