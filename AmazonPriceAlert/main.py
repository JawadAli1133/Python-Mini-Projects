from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup
import smtplib


SMTP_ADDRESS = 'smtp.gmail.com'
EMAIL_ADDRESS = 'jawadaliamjadali664@gmail.com'
EMAIL_PASSWORD = 'xqqgyoxklyqhamoq'


# url = 'https://appbrewery.github.io/instant_pot/'
url = 'https://www.amazon.com/MSI-Keyboard-Included-Friendly-Home-Adv/dp/B0CDKLKC2G/ref=sr_1_1?crid=24SGWP4EQVGPB&dib=eyJ2IjoiMSJ9.SzTMvVzT8Rm5EXJzt5QvG7IylYRVNcl-vLjUAXcrDM2ToWEScmQP3G5vSB4OO4s0d_XbOp0aoNbvENtIKv9-uBuhF2qCQnzjBDr-94FydvdnZFtdk5A6dB8ZLRbkzblsR6F23xSsv8NtjbWM_l2B-18vTQCvMgw22vaS-q0ltUoOxN5G7rgt38MYV5YOPVABFBkQPQaI5-tP409QHR5b7Syx25OHAgOegwlhgB90Y6U.vLutKot1uw_lJzsqEbv-wkozN_cB7S-mBIOg608_oao&dib_tag=se&keywords=pc&qid=1722606490&sprefix=p%2Caps%2C298&sr=8-1'

response = requests.get(url)
amazon_html = response.text
soup = BeautifulSoup(amazon_html, 'html.parser')
price = soup.find(name='span', class_='a-offscreen').text
price_without_currency = float(price.split('$')[1])
product_name = soup.find(name='span', id='productTitle').text
print(price_without_currency)
print(product_name)


if price_without_currency < 1000:
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'jawadaliamjad1641@yahoo.com'
    msg['Subject'] = 'Amazon Price Alert'

    body = f'{product_name} is now ${price_without_currency}\n{url}'
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    connection.send_message(msg)
    connection.close()
else:
    print("Do not buy now.")

