import csv

from datetime import datetime

from birthday import Birthday
from birthday_list import assemble_birthday_list


def read_jarig_file() -> list:
    with open('jarig.csv') as csv_file:
        birthdays = []
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            birthday = row["birthday"].strip().split('-')
            day = int(birthday[0])
            month = int(birthday[1])
            year = None
            if len(birthday) > 1:
                if birthday[2] != '1900':
                    year = int(birthday[2])
            birthdays.append(Birthday(name=row["name"], day=day, month=month, year=year))
            line_count += 1
    return birthdays


# birthdays = read_jarig_file()
# print(birthdays)
# today = datetime(2022, 6, 29)
# party_list = assemble_birthday_list(birthdays, today, 20, 10)
#
# for party in party_list:
#     print(party['name'], party['party_date'], party['age'] if 'age' in party else "?")
