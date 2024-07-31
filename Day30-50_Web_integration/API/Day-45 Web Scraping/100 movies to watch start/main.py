import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

scrapped_info = response.text

soup = BeautifulSoup(scrapped_info, "html.parser")

movieslist =[item.getText() for item in soup.find_all("h3", class_="listicleItem_listicle-item__title__BfenH")]

movieslist.reverse()

print(movieslist)

with open ("Movie-List.txt", "w") as file:
    for movie in movieslist:
        file.write(f"{movie}\n")



