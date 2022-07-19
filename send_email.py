import smtplib
import ssl
import datetime
import locale
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from birthday_list import assemble_birthday_list
from file_interface import read_jarig_file
from secrets import EMAIL_PASSWORD, LOGIN_EMAIL

PORT = 465
SENDER_EMAIL = "info@jarig.org"
SMTP_URL = "smtp.dds.nl"
SUBJECT = "Verjaardagen!"

def label(party: dict) -> str:
    locale.setlocale(locale.LC_TIME, "nl_NL")
    party_date = party["party_date"].strftime('%A %d %B')
    label_text = f'{party["name"]}: {party_date}'
    if 'age' in party:
        return f'{party["name"]} ({party["age"]}): {party_date}'
        # return label_text + f' ({party["age"]})\n'
    else:
        return f'{party["name"]}: {party_date}'
        # return label_text + '\n'


def make_mail_body(filename: str, reference_date: datetime) -> (str, str):
    text = ""
    html = "<html>" \
           "   <body>" \
           "      <p>"

    birthdays = read_jarig_file(filename)

    party_list = assemble_birthday_list(birthdays, reference_date, 10, 10)
    for party in party_list:
        if party["party_date"] < reference_date.date():
            text += label(party) + "\n"
            html += label(party) + "<br>\n"
        elif party["party_date"] == reference_date.date():
            text += label(party) + "\n"
            html += "<font color='red'>" + label(party) + "</font><br>\n"
        else:
            text += label(party) + "\n"
            html += label(party) + "<br>\n"

    html += """\
                </p>\
            </body>\
        </html>\
    """
    return text, html


def send_jarig_mail(receiver_email, text, html):
    password = EMAIL_PASSWORD

    message = MIMEMultipart('alternative')
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_URL, PORT, context=context) as server:
        server.login(LOGIN_EMAIL, password)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())


if __name__ == "__main__":
    # today = datetime.datetime(2022, 7, 18)
    today = datetime.datetime.now()
    text, html = make_mail_body('jarig.csv', today)
    receiver_email = "jarig@vpathuis.dds.nl"
    send_jarig_mail(receiver_email, text, html)
    print(html)


