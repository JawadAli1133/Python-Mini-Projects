import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_html = response.text

soup = BeautifulSoup(empire_html, 'html.parser')
movies_div = soup.find(name='div', class_='entity-info-items__list')
movies_list = [movie.getText() for movie in movies_div.find_all('a')]

for i in range(len(movies_list)):
    with open('movies.txt', 'a') as file:
        file.write(f'{i+1}) {movies_list[i]}\n')

