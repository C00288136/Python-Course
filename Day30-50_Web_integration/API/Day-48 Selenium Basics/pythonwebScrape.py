from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

div = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]')

times = div.find_elements(By.TAG_NAME, value="time")

names = div.find_elements(By.TAG_NAME, value="a")

upcoming_events_dict = {}

for i in range(len(times)):
    upcoming_events_dict[i] = {"time": times[i].text, "name" : names[i].text}


print(upcoming_events_dict)

    
driver.quit()