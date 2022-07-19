from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Birthday:
    """
    This is a name, day and month with optionally a year.
    Birthdays come this way: either you know the year of birth, or not
    If the year is know, also the age can be calculated.
    """

    @property
    def name(self):
        return self._name

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def age(self, reference_date: datetime):
        if self.year:
            return relativedelta(reference_date, self.as_datetime()).years

    def is_birthday(self, reference_date: datetime):
        return self.month == reference_date.month and self.day == reference_date.day

    def in_range(self, reference_date: datetime, offset_past: int, offset_future: int):
        """ This returns a datetime within the offsets from date """
        for offset in range(-offset_past, offset_future + 1):
            offset_date = (reference_date + timedelta(days=offset)).date()
            if offset_date.month == self.month and offset_date.day == self.day:
                return offset_date
        return

    def as_datetime(self):
        """Returns the Birthday date a datetime object, unless the year is not know"""
        if self.year:
            return datetime(year=self.year, month=self.month, day=self.day)

    def __init__(self, name: str, day: int, month: int, year: int = None):
        self._name = name
        self._day = day
        self._month = month
        self._year = year

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name},day={self.day},month={self.month},year={self.year})"

    def __str__(self):
        return self.__format__("")

    def __eq__(self, other):
        return \
            self.name == other.name and \
            self.day == other.day and \
            self.month == other.month and \
            self.year == other.year

    def __format__(self, spec):
        if self.year:
            return f"{self.name}: {self.day}-{self.month}-{self.year}"
        else:
            return f"{self.day}-{self.month}"


if __name__ == "__main__":
    p1 = Birthday(name='piet', year=1975, month=12, day=29)
    today = datetime.now()
    print('today: ', today)
    print('bd1:', repr(p1))
    print('bd1:', p1, '(' + str(p1.age(today)) + ')')
    print('today:', p1.is_birthday(today))
    party_date = p1.in_range(today, 250, 25)
    if party_date:
        print('party date:', party_date)