import unittest
from datetime import datetime

from birthday_list import assemble_birthday_list
from birthday import Birthday


class BirthdayListTestCase(unittest.TestCase):
    def test_birthday_list(self):
        bd1 = Birthday(name='Aad', year=1975, month=12, day=1)
        bd2 = Birthday(name='Bert', year=1975, month=12, day=2)
        bd3 = Birthday(name='Claudia', month=12, day=3)
        bdl = [bd1, bd2, bd3]

        self.assertEqual(Birthday(name='Aad', day=1, month=12, year=1975), bdl[0])
        self.assertEqual(Birthday(name='Bert', day=2, month=12, year=1975), bdl[1])
        self.assertEqual(Birthday(name='Claudia', day=3, month=12), bdl[2])

    def test_birthday_list_near_birthdays(self):
        bd1 = Birthday(name='Aad', year=1975, month=12, day=1)
        bd2 = Birthday(name='Bert', year=1975, month=12, day=2)
        bd3 = Birthday(name='Claudia', month=12, day=3)
        bdl = [bd1, bd2, bd3]

        today = datetime(2022, 12, 4)
        near_birthdays = assemble_birthday_list(bdl, today, 2, 2)
        self.assertEqual('Bert', near_birthdays[0]['name'])
        self.assertEqual(datetime(2022, 12, 2).date(), near_birthdays[0]['party_date'])
        self.assertEqual(47, near_birthdays[0]['age'])
        self.assertEqual('Claudia', near_birthdays[1]['name'])
        self.assertEqual(datetime(2022, 12, 3).date(), near_birthdays[1]['party_date'])
        self.assertNotIn('age', near_birthdays[1])


if __name__ == "__main__":
    unittest.main()
