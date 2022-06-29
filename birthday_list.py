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
