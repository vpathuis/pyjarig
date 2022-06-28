import unittest
from datetime import datetime

from birthday_list import BirthdayList
from birthday import Birthday


class BirthdayListTestCase(unittest.TestCase):
    def test_birthday_list(self):
        bd1 = Birthday(year=1975, month=12, day=1)
        bd2 = Birthday(year=1975, month=12, day=2)
        bd3 = Birthday(month=12, day=3)
        bdl = [bd1, bd2, bd3]

        bla = BirthdayList(bdl)
        self.assertEqual(Birthday(day=1, month=12, year=1975), bla[0])
        self.assertEqual(Birthday(day=2, month=12, year=1975), bla[1])
        self.assertEqual(Birthday(day=3, month=12), bla[2])

    def test_birthday_list_near_birthdays(self):
        bd1 = Birthday(year=1975, month=12, day=1)
        bd2 = Birthday(year=1975, month=12, day=2)
        bd3 = Birthday(month=12, day=3)
        bdl = [bd1, bd2, bd3]
        today = datetime(2022, 12, 4)
        bla = BirthdayList(bdl)
        near_birthdays = bla.near_birthdays(today, 2, 2)
        self.assertEqual(Birthday(day=2, month=12, year=1975), near_birthdays[0])
        self.assertEqual(Birthday(day=3, month=12), near_birthdays[1])


if __name__ == "__main__":
    unittest.main()
