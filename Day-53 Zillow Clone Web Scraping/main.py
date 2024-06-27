from bs4 import BeautifulSoup
from time import sleep
import requests
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


website = requests.get("https://appbrewery.github.io/Zillow-Clone/").text

FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScgpvrRUcmxWzxkRd_VpJtBkOfXoSwRKU-nenIJ1kwx-kRxug/viewform?usp=sf_link"


soup = BeautifulSoup(website, "html.parser")

# info_div = soup.find_all("ul", class_="List-c11n-8-84-3-photo-cards").text




def price_list():
    property_price = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")

    price_list = []

    for price in property_price:
        parts = price.text.split('+')
        price_format1 = parts[0]
        parts2 = price_format1.split("/")
        formatted_price = str(parts2[0])
        price_list.append(formatted_price)
    return price_list

def property_links_list():
    property_link = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
    # list of links for properties
    property_links_list = []

    for link in property_link:
        property_links_list.append(link["href"])
    return property_links_list

def property_addresses():

    property_addresses = soup.find_all("address")

    address_list = []

    for address in property_addresses:
        address_list.append(address.text.strip())
    return address_list


prices = price_list()
links = property_links_list()
addresses = property_addresses()




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORMS_LINK)

for i in range(len(prices)):
    try:
        sleep(4)
        address_in = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_in.send_keys(addresses[i])

        price_in = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_in.send_keys(prices[i])

        link_in = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_in.send_keys(links[i])

        submit_but = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_but.click()
        sleep(1)
        another_response = driver.find_element(By.LINK_TEXT, value="Submit another response")
        another_response.click()
        sleep(1)
    except Exception as e:
        print(f"A error occured: {e}")
        break