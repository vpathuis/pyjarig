import tkinter
import datetime

from birthday_list import assemble_birthday_list
from file_interface import read_jarig_file

def label(party: dict) -> str:
    label_text = f'{party["name"]}: {party["party_date"]}'
    if party['age']:
        return label_text + f' ({party["age"]})\n'
    else:
        return label_text + '\n'


birthdays = read_jarig_file()
today = datetime.datetime.now()
party_list = assemble_birthday_list(birthdays, today, 10, 10)
print(party_list)
label_past = ""
label_today = ""
label_future = ""
for party in party_list:
    if party["party_date"] < today.date():
        print("past:", party)
        label_past += label(party)
    elif party["party_date"] == today.date():
        print("today:", party)
        label_today += label(party)
    else:
        print("future:", party)
        label_future += label(party)


window = tkinter.Tk()
bd_label_past = tkinter.Label(window, text=label_past)
bd_label_today = tkinter.Label(window, text=label_today)
bd_label_future = tkinter.Label(window, text=label_future)
bd_label_past.pack()
bd_label_today.pack()
bd_label_future.pack()
window.title("Jarig")
window.mainloop()