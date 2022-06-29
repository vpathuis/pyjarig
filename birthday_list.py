from datetime import datetime

from birthday import Birthday


def assemble_birthday_list(birthdays: list, reference_date: datetime, past_days: int, future_days: int) -> list:
    near_birthdays = []
    for birthday in birthdays:
        party_date = birthday.in_range(reference_date, past_days, future_days)
        if party_date:
            near_birthday = {
                'name': birthday.name,
                'party_date': party_date
            }
            if birthday.year:
                near_birthday['age'] = birthday.age(reference_date)
            near_birthdays.append(near_birthday)
    return near_birthdays
#
# class BirthdayList(list):
#     """Assemble the dict with relevant birthdays
#        Accepts a list of party_people (names and birthdays)."""
# # IDEE: NearBirthdays de class laten zijn, overerfen van list. Wat voegt BirthdayList nog toen als class?
#     # @property
#     # def list(self):
#     #     return self._party_people
#
#     def near_birthdays(self, date: datetime, past_days: int, future_days: int):
#         near_birthdays = []
#         for birthday in self:
#             if birthday.in_range(date, past_days, future_days):
#                 near_birthdays.append(birthday)
#         return near_birthdays
#
#     # def append(self, name, birthday):
    #     self._party_people[name] = birthday
    #
    # def __init__(self, party_people: list):
    #     self._party_people = party_people
    #     super()
    #
    # def __repr__(self):
    #     return f"BirthdayList({self._party_people})"
    #
    # def __str__(self):
    #     return str(self._party_people)
    #
    # def __getitem__(self, index):
    #     return self._party_people[index5]


# bd1 = Birthday(name='piet', year=1975, month=12, day=1)
# bd2 = Birthday(name='kees', year=1975, month=12, day=2)
# bd3 = Birthday(name='lies', month=12, day=3)
# birthdays = [bd1, bd2, bd3]
# print(repr(birthdays))
#
# today = datetime(2022, 12, 4)
#
# bl = assemble_birthday_list(birthdays, today, 2, 2)
# for party in bl:
#     print(party)
