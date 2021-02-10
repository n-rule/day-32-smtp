import smtplib
import datetime as dt
from random import choice

with open('quotes.txt') as quotes:
    # list_of_quotes = [line.strip() for line in quotes]
    list_of_quotes = quotes.readlines()

random_quote = choice(list_of_quotes)

date_of_birth = dt.datetime(year=1986, month=1, day=11, hour=4, minute=15)

my_email = 'ffdeimos2ua@gmail.com'
password = ''

now = dt.datetime.now()

if now.weekday() == 2:

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='rule@ukr.net',
            msg=f'subject:Wednesday motivation for cocksuckers\n\n{random_quote}')

