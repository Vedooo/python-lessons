import requests as rq
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = rq.get(url)
web_html = response.text
soup = BeautifulSoup(web_html, 'html.parser')

all_movies = soup.find_all(name='h3', class_='title')

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f'{movie}\n')