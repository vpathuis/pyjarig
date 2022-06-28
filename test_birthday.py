import unittest

from birthday import Birthday


class BirthdayTestCase(unittest.TestCase):
    def test_birthday(self):
        bd1 = Birthday(year=1975, month=12, day=2)
        bd2 = Birthday(month=12, day=3)
        self.assertEqual(Birthday(year=1975, month=12, day=2), bd1)
        self.assertEqual(Birthday(month=12, day=3), bd2)
        self.assertNotEqual(bd1, bd2)
        self.assertEqual(2, bd1.day)
        self.assertEqual(12, bd1.month)
        self.assertEqual(1975, bd1.year)
        self.assertEqual(None, bd2.year)


if __name__ == '__main__':
    unittest.main()
