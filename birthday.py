class Birthday:
    """This is a day + month with optionally a year.
    Birthdays come this way: either you know the year of birth, or not"""

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def __init__(self, day: int, month: int, year: int = None):
        self._day = day
        self._month = month
        self._year = year

    def __repr__(self):
        return f"{type(self).__name__}(day={self._day},month={self._month},year={self._year})"

    def __str__(self):
        return self.__format__("")

    def __eq__(self, other):
        return \
            self.day == other.day and self.month == other.month and self.year == other.year

    def __format__(self, spec):
        month = self._month
        if self._year:
            return f"{self._day}-{month}-{self._year}"
        else:
            return f"{self._day}-{month}"
