from bs4 import BeautifulSoup
import requests


url = requests.get("https://news.ycombinator.com/news")

yc_web_page = url.text


soup = BeautifulSoup(yc_web_page,"html.parser")

article_tag = soup.find("span",class_="titleline")


article_anchor = article_tag.find("a")

article_score = soup.find("span", class_="score")

print(article_score.getText())



