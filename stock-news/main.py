from twilio.rest import Client
import requests


API_KEY = 'D6BJGEKFWF4LXMAL'
URL = 'https://www.alphavantage.co/query'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_URL = 'https://newsapi.org/v2/everything'
ACC_ID = 'AC56bb9e0cd96e48af5c973b115cd91324'
AUTH_TK = '5cad41ec93723829e31feebea056bd7b'

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY
}

news_parameters = {
    'qInTitle': COMPANY_NAME,
    'apiKey': 'aea527a41ff748f4a4ed82dea6f412af'
}


def get_news():
    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    three_articles = news_data[:3]
    return three_articles


response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
time_series_data = data['Time Series (Daily)']
last_two_days_data = list(time_series_data.items())[:2]
yesterday_close = float(last_two_days_data[0][1]['4. close'])
day_before_yesterday_close = float(last_two_days_data[1][1]['4. close'])
percentage_change = ((yesterday_close-day_before_yesterday_close) / day_before_yesterday_close) * 100

message = ''
if percentage_change > 0:
    message += f'TSLA: 🔺{abs(percentage_change)}%\n'
else:
    message += f'TSLA: 🔻{abs(percentage_change)}%\n'

articles = get_news()
for i in range(len(articles)-1):
    message += f'Article: 0{i+1}\n'
    message += f'Title: {articles[i]["title"]}\n'
    message += f'Title: {articles[i]["description"]}\n'
print(message)

# client = Client(ACC_ID, AUTH_TK)
# msg = client.messages.create(
#     body=str(message),
#     from_='+12295973444',
#     to='+923260111641')



































# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


