import smtplib
import datetime as dt
import random as ran

my_email = 'jawadaliamjadali664@gmail.com'
password = 'xqqgyoxklyqhamoq'

with open('quotes.txt') as file:
    quotes = file.readlines()
if dt.datetime.now().weekday() == 4:
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)

    subject = 'Test Email'
    body = ran.choice(quotes)
    msg = f'Subject: {subject}\n\n{body}'

    connection.sendmail(from_addr=my_email, to_addrs='jawadaliamjad1641@yahoo.com', msg=msg)
    connection.close()
else:
    print("May be another day.")

