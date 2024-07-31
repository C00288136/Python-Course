from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


articles_num = driver.find_element(By.ID, value="articlecount")

number = articles_num.text.split("a")[0]

search = driver.find_element(By.NAME, value="search")

# enters keyboard input into the search field
search.send_keys("Python", Keys.ENTER)


print(number)


driver.quit()