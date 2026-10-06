import requests
from bs4 import BeautifulSoup
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


content_html = requests.get(url)

soup = BeautifulSoup(markup=content_html.text, features="lxml")
films = []
all_films = soup.find_all(name="h3", class_="title")
for film in all_films:
    films.append(film.get_text())

reversed_films = films[::-1]

with open('100_best_films.txt', 'w') as file:
    for film in reversed_films:
        file.write(film.encode("ascii", "ignore").decode("ascii"))
        file.write('\n')

print("Done")