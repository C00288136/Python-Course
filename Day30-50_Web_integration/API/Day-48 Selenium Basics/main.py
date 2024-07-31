from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.co.uk/gp/product/B01J1GHT1G/ref=ox_sc_saved_title_10?smid=A3M5PB0EF6U9O2&th=1")

price_pound = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"Price is {price_pound.text}.{price_cent.text}")
# this is used when there is no easy way of getting to the anchor for example 
# because it doesnt have a id or class
# driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# USING XPATH
# using xpath if we cant find the element using any other method
link = driver.find_element(By.XPATH, value='//*[@id="nav-recently-viewed"]/span[1]')
print(link.text)


# closes the whole browser
driver.quit()
# # closes the tab
# driver.close()