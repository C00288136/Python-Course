from bs4 import BeautifulSoup
import requests
import pprint


website = requests.get("https://appbrewery.github.io/Zillow-Clone/").text

FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScgpvrRUcmxWzxkRd_VpJtBkOfXoSwRKU-nenIJ1kwx-kRxug/viewform?usp=sf_link"


soup = BeautifulSoup(website, "html.parser")

# info_div = soup.find_all("ul", class_="List-c11n-8-84-3-photo-cards").text

property_price = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")


for price in property_price:
    pprint.pprint(price)






