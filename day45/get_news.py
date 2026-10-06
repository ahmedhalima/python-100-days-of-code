import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/news.ycombinator.com/"

website_content = requests.get(url)

soup = BeautifulSoup(markup=website_content.text, features="lxml")

news_urls = soup.find_all(class_="storylink")

for link in news_urls:
    print(link.text)
    print(link.get('href'))
