import requests
import datetime as dt
import smtplib
import time


MY_LAT = 51.507351
MY_LNG = -0.127758

parameter = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}


def is_iss_overhead():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_longitude = float(iss_data['iss_position']['longitude'])
    iss_latitude = float(iss_data['iss_position']['latitude'])

    if MY_LAT+5 >= iss_latitude >= MY_LAT-5 and MY_LNG + 5 >= iss_longitude >= MY_LNG-5:
        return True


def is_nighttime():
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]
    hour = dt.datetime.now().hour
    if hour >= sunset or hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        my_email = 'jawadaliamjadali664@gmail.com'
        password = 'xqqgyoxklyqhamoq'

        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        subject = 'ISS is Overhead'
        msg_body = 'ISS is Overhead\n\nAlso it is the night time\nSo go out and watch it.'
        msg = f'Subject: {subject}\n\n{msg_body}'
        connection.sendmail(from_addr=my_email, to_addrs='jawadaliamjad1641@yahoo.com', msg=msg)
        connection.close()
        break
