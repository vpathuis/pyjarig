from datetime import datetime

from flask import Flask

from birthday_list import assemble_birthday_list, format_party_list
from file_interface import read_jarig_file

app = Flask(__name__)


@app.route('/')
def jarig():
    birthdays = read_jarig_file()
    today = datetime.now()
    party_list = assemble_birthday_list(birthdays, today, 20, 10)

    past, current, future = format_party_list(party_list, today)
    html = ""
    for bd in past:
        html += bd + "<br>\n"
    html += "<b>"
    for bd in current:
        html += bd + "<br>\n"
    html += "</b>"
    for bd in future:
        html += bd + "<br>\n"
    return html

# print(jarig())
