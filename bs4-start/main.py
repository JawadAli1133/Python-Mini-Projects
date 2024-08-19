from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'https://appbrewery.github.io/news.ycombinator.com/'
# url = 'https://news.ycombinator.com/news'

response = requests.get(url)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,'html.parser')
anchors = soup.find_all(name='a', class_='storylink')


scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
maximum = 0
index = -1
for i in range(len(scores)):
    if scores[i] > maximum:
        maximum = scores[i]
        index = i
print("The one with highest score is :")
print(anchors[index].getText())
print(anchors[index].get('href'))













































# import lxml
#
# with open('website.html', encoding='utf-8') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'lxml')
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags[0].get('href'))
#
# heading = soup.find_all(name='h1',id='name')
# print(heading[0].getText())
#
# h1 = soup.select_one(selector='#name')
# print(h1)
