from datetime import datetime
import unittest

import calculations
from birthday import Birthday


class CalculationsTestCase(unittest.TestCase):
    def test_is_birthday(self):
        birthday = datetime.strptime("02-12-1975", "%d-%m-%Y")
        self.assertEqual(
            False,
            calculations.is_birthday(
                datetime.strptime("31-01-2023", "%d-%m-%Y"), birthday
            ),
        )
        self.assertEqual(
            False,
            calculations.is_birthday(
                datetime.strptime("01-12-2022", "%d-%m-%Y"), birthday
            ),
        )
        self.assertEqual(
            True,
            calculations.is_birthday(
                datetime.strptime("02-12-2022", "%d-%m-%Y"), birthday
            ),
        )

    def test_age(self):
        birthday = datetime.strptime("02-12-1975", "%d-%m-%Y")
        self.assertEqual(
            47,
            calculations.calculate_age(
                datetime.strptime("31-01-2023", "%d-%m-%Y"), birthday
            ),
        )
        self.assertEqual(
            46,
            calculations.calculate_age(
                datetime.strptime("01-12-2022", "%d-%m-%Y"), birthday
            ),
        )
        self.assertEqual(
            47,
            calculations.calculate_age(
                datetime.strptime("02-12-2022", "%d-%m-%Y"), birthday
            ),
        )

    def test_birthday_in_range(self):
        """Test is the range is calculated right in all cases"""

        # check for dates at the end of the year
        date = datetime(2022, 12, 31)
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(29, 12), date, 1, 1)
        )
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(2, 1), date, 1, 1)
        )
        date = datetime(2022, 12, 30)
        self.assertEqual(
            datetime(2022, 12, 30),
            calculations.birthday_in_range(Birthday(30, 12), date, 0, 0),
        )
        self.assertEqual(
            datetime(2022, 12, 31),
            calculations.birthday_in_range(Birthday(31, 12), date, 0, 1),
        )
        self.assertEqual(
            datetime(2023, 1, 2),
            calculations.birthday_in_range(Birthday(2, 1), date, 0, 3),
        )
        self.assertEqual(
            datetime(2022, 12, 25),
            calculations.birthday_in_range(Birthday(25, 12), date, 5, 0),
        )

        # check for dates at the end beginning the year
        date = datetime(2022, 1, 1)
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(30, 12), date, 1, 1)
        )
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(3, 1), date, 1, 1)
        )
        date = datetime(2022, 1, 2)
        self.assertEqual(
            datetime(2022, 1, 2),
            calculations.birthday_in_range(Birthday(2, 1), date, 0, 0),
        )
        self.assertEqual(
            datetime(2022, 1, 1),
            calculations.birthday_in_range(Birthday(1, 1), date, 1, 0),
        )
        self.assertEqual(
            datetime(2021, 12, 31),
            calculations.birthday_in_range(Birthday(31, 12), date, 2, 0),
        )
        self.assertEqual(
            datetime(2022, 1, 7),
            calculations.birthday_in_range(Birthday(7, 1), date, 0, 5),
        )

        # check when it is a leap day
        date = datetime(2020, 2, 29)
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(27, 2), date, 1, 1)
        )
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(3, 2), date, 1, 1)
        )
        self.assertEqual(
            datetime(2020, 2, 29),
            calculations.birthday_in_range(Birthday(29, 2), date, 0, 0),
        )
        self.assertEqual(
            datetime(2020, 2, 28),
            calculations.birthday_in_range(Birthday(28, 2), date, 1, 0),
        )
        self.assertEqual(
            datetime(2020, 3, 1),
            calculations.birthday_in_range(Birthday(1, 3), date, 0, 1),
        )
        self.assertEqual(
            datetime(2020, 3, 4),
            calculations.birthday_in_range(Birthday(4, 3), date, 0, 5),
        )

        # check when it is around a leap day
        date = datetime(2020, 2, 28)
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(26, 2), date, 1, 1)
        )
        self.assertEqual(
            None, calculations.birthday_in_range(Birthday(1, 3), date, 1, 1)
        )
        self.assertEqual(
            datetime(2020, 2, 28),
            calculations.birthday_in_range(Birthday(28, 2), date, 0, 0),
        )
        self.assertEqual(
            datetime(2020, 2, 29),
            calculations.birthday_in_range(Birthday(29, 2), date, 0, 1),
        )
        self.assertEqual(
            datetime(2020, 3, 1),
            calculations.birthday_in_range(Birthday(1, 3), date, 0, 2),
        )
        self.assertEqual(
            datetime(2020, 3, 4),
            calculations.birthday_in_range(Birthday(4, 3), date, 0, 6),
        )


if __name__ == "__main__":
    unittest.main()
