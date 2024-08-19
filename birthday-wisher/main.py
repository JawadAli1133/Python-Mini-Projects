import smtplib
import random as ran
import pandas
import datetime as dt

letters = {
    1 : 'letter_1.txt',
    2: 'letter_2.txt',
    3: 'letter_3.txt',
}
# Hard Starting Project

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


def create_letter(name):
    filename = letters[ran.randint(1, 3)]
    file_path = f'letter_templates/{filename}'
    with open(file_path) as file:
        content = file.read()
    content = content.replace('[NAME]', name)
    return content


def send_mail(mail, msg_body):
    my_email = 'jawadaliamjadali664@gmail.com'
    my_password = 'xqqgyoxklyqhamoq'

    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    subject = 'Happy birthday Wishes'
    msg_body = str(msg_body)
    msg: str = f'Subject: {subject}\n\n{msg_body}'
    connection.sendmail(from_addr=my_email, to_addrs=mail, msg=msg)
    connection.close()


birthday_data = pandas.read_csv('birthdays.csv')
birthday_persons = birthday_data.to_dict(orient='records')
for person in birthday_persons:
    if person['month'] == dt.datetime.now().month and person['day'] == dt.datetime.now().day:
        msg = create_letter(person['name'])
        mail = person['email']
        send_mail(mail, msg)

