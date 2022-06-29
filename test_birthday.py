import unittest
from datetime import datetime

from birthday import Birthday


class BirthdayTestCase(unittest.TestCase):
    def test_birthday(self):
        bd1 = Birthday(name='aad', year=1975, month=12, day=2)
        bd2 = Birthday(name='bert', month=12, day=3)
        self.assertEqual(Birthday(name='aad', year=1975, month=12, day=2), bd1)
        self.assertEqual(Birthday(name='bert', month=12, day=3), bd2)
        self.assertNotEqual(bd1, bd2)
        self.assertEqual('aad', bd1.name)
        self.assertEqual(2, bd1.day)
        self.assertEqual(12, bd1.month)
        self.assertEqual(1975, bd1.year)
        self.assertEqual(None, bd2.year)

    def test_age(self):
        # test age when birth year is known
        birthday = Birthday(name='aad', year=1975, month=12, day=2)
        self.assertEqual(
            47,
            birthday.age(datetime(2023,1,31)),
        )
        self.assertEqual(
            46,
            birthday.age(datetime(2022,12,1)),
        )
        self.assertEqual(
            47,
            birthday.age(datetime(2022,12,2)),
        )

        # test age when birth year unknown
        birthday = Birthday(name='aad', month=12, day=2)
        self.assertEqual(
            None,
            birthday.age(datetime(2023,1,31)),
        )

    def test_birthday_in_range(self):
        """Test is the range is calculated right in all cases"""

        # check for dates at the end of the year
        date = datetime(2022, 12, 31)
        self.assertEqual(
            None, Birthday('', day=29, month=12).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            None, Birthday('', day=2, month=1).in_range(reference_date=date, offset_past=1, offset_future=1)
        )

        date = datetime(2022, 12, 30)
        self.assertEqual(
            datetime(2022, 12, 30).date(),
            Birthday('', day=30, month=12).in_range(reference_date=date, offset_past=0, offset_future=0)
        )
        self.assertEqual(
            datetime(2022, 12, 31).date(),
            Birthday('', day=31, month=12).in_range(reference_date=date, offset_past=0, offset_future=1)
        )
        self.assertEqual(
            datetime(2023, 1, 2).date(),
            Birthday('', day=2, month=1).in_range(reference_date=date, offset_past=0, offset_future=3)
        )
        self.assertEqual(
            datetime(2022, 12, 25).date(),
            Birthday('', day=25, month=12).in_range(reference_date=date, offset_past=5, offset_future=0)
        )

        # check for dates at the end beginning the year
        date = datetime(2022, 1, 1)

        self.assertEqual(
            None,
            Birthday('', day=30, month=12).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            None,
            Birthday('', day=3, month=1).in_range(reference_date=date, offset_past=1, offset_future=1)
        )

        date = datetime(2022, 1, 2)

        self.assertEqual(
            datetime(2022, 1, 2).date(),
            Birthday('', day=2, month=1).in_range(reference_date=date, offset_past=0, offset_future=0)
        )
        self.assertEqual(
            datetime(2022, 1, 1).date(),
            Birthday('', day=1, month=1).in_range(reference_date=date, offset_past=1, offset_future=0)
        )
        self.assertEqual(
            datetime(2021, 12, 31).date(),
            Birthday('', day=31, month=12).in_range(reference_date=date, offset_past=2, offset_future=0)
        )
        self.assertEqual(
            datetime(2022, 1, 7).date(),
            Birthday('', day=7, month=1).in_range(reference_date=date, offset_past=0, offset_future=5)
        )

        # check when it is a leap day
        date = datetime(2020, 2, 29)

        self.assertEqual(
            None,
            Birthday('', day=27, month=2).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            None,
            Birthday('', day=2, month=3).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            datetime(2020, 2, 29).date(),
            Birthday('', day=29, month=2).in_range(reference_date=date, offset_past=0, offset_future=0)
        )
        self.assertEqual(
            datetime(2020, 2, 28).date(),
            Birthday('', day=28, month=2).in_range(reference_date=date, offset_past=1, offset_future=0)
        )
        self.assertEqual(
            datetime(2020, 3, 1).date(),
            Birthday('', day=1, month=3).in_range(reference_date=date, offset_past=0, offset_future=1)
        )
        self.assertEqual(
            datetime(2020, 3, 4).date(),
            Birthday('', day=4, month=3).in_range(reference_date=date, offset_past=0, offset_future=5)
        )

        # check when it is around a leap day
        date = datetime(2020, 2, 28)
        self.assertEqual(
            None,
            Birthday('', day=26, month=2).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            None,
            Birthday('', day=1, month=3).in_range(reference_date=date, offset_past=1, offset_future=1)
        )
        self.assertEqual(
            datetime(2020, 2, 28).date(),
            Birthday('', day=28, month=2).in_range(reference_date=date, offset_past=0, offset_future=0)
        )
        self.assertEqual(
            datetime(2020, 2, 29).date(),
            Birthday('', day=29, month=2).in_range(reference_date=date, offset_past=0, offset_future=1)
        )
        self.assertEqual(
            datetime(2020, 3, 1).date(),
            Birthday('', day=1, month=3).in_range(reference_date=date, offset_past=0, offset_future=2)
        )
        self.assertEqual(
            datetime(2020, 3, 4).date(),
            Birthday('', day=4, month=3).in_range(reference_date=date, offset_past=0, offset_future=6)
        )

if __name__ == '__main__':
    unittest.main()
