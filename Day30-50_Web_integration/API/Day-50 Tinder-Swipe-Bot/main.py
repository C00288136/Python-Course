from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException



load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()
time.sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="q-314954669"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)
time.sleep(2)
email = driver.find_element(By.NAME, value="email")
email.send_keys(os.environ["email"])
time.sleep(2)
password = driver.find_element(By.NAME, value="pass")
password.send_keys(os.environ["password"])
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(10)

allow_location = driver.find_element(By.XPATH, value='//*[@id="q-314954669"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]/div')
allow_location.click()
time.sleep(1)
allow_cookies = driver.find_element(By.XPATH, value='//*[@id="q-314954669"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
allow_cookies.click()
time.sleep(3)
no_notifications = driver.find_element(By.XPATH, value='//*[@id="q-314954669"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
no_notifications.click()
time.sleep(10)
likes = 0
for n in range(100):
        time.sleep(2)
        try:
                print("Clicking the Like button...")
                heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
                heart_icon.click()

    # For "It's a match" pop-up!
        except ElementClickInterceptedException:
                try:
                        match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                        match_popup.click()
        # For "Tinder Gold" pop-up
                except NoSuchElementException:
                        close_tinder_gold = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button")
                        close_tinder_gold.click()

    # If the Like button changes XPath after the first Like
        except NoSuchElementException:
                try:
                        heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
                        heart_icon.click()
                # For "Add Tinder to your Home Screen" pop-up
                except ElementClickInterceptedException:
                        not_interested_button = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div")
                        not_interested_button.click()

    
