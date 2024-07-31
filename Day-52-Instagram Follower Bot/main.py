from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv()



SIMILARACCOUNT = "coding"

class InstaFollower:

# chrome options leave the browser open helps with bug fixes
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)


# function to log into instagram
    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        cookies = self.driver.find_element(By.CSS_SELECTOR, value='._a9_1')
        cookies.click()
        sleep(1)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(os.environ["USERNAME"])
        sleep(1)
        password= self.driver.find_element(By.NAME, value="password")
        password.send_keys(os.environ["PASSWORD"], Keys.ENTER)
        sleep(6)
        cookies = self.driver.find_element(By.CSS_SELECTOR, value=".xqeqjp1")
        cookies.click()
        sleep(2)
        notifications = self.driver.find_element(By.CSS_SELECTOR, value='._a9_1')
        sleep(1)
        


# function to search for the page and open followers list
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILARACCOUNT}")
        sleep(3)
        followrs_button =self.driver.find_element(By.XPATH, value= "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x2b8uid x10wh9bi x1wdrske x8viiok x18hxmgj']")
        followrs_button.click()
        # scroll_area = self.driver.find_element(By.CSS_SELECTOR, value='.xz65tgg')
        # action = ActionChains(self.driver)
        # action.move_to_element(scroll_area)
        # action.perform()

        # sleep(5)


        

# function to follow the users
    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()