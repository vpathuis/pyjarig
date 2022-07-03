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


def format_party_item(party: dict) -> str:
    text = f'{party["name"]}: {party["party_date"]}'
    if 'age' in party:
        return text + f' ({party["age"]})'
    else:
        return text

def format_party_list(party_list: list, reference_date: datetime) -> (list, list, list):
    """Creates three formatted lists with past, current and future birthdays from the party-list"""
    list_past = []
    list_today = []
    list_future = []
    for party in party_list:
        if party["party_date"] < reference_date.date():
            list_past.append(format_party_item(party))
        elif party["party_date"] == reference_date.date():
            list_today.append(format_party_item(party))
        else:
            list_future.append(format_party_item(party))

    return list_past, list_today, list_future

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
