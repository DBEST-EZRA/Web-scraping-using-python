import requests
from bs4 import BeautifulSoup

url = 'https://www.onekitty.co.ke/'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

titles = soup.find_all('h2', class_='post-title')

for index, title in enumerate(titles, start=1):
    print(f"{index}. {title.get_text()}")

titles_list = [title.get_text() for title in titles]

with open('titles.txt', 'w') as file:
    for title in titles_list:
        file.write(f"{title}\n")

print("Titles extracted and saved.")

