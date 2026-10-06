from bs4 import BeautifulSoup

with open('website.html') as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "lxml")
all_anchor_tags = soup.find_all('a')

for tag in all_anchor_tags:
    print(tag.get('href'))