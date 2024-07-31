from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

PROMISED_DOWN = 500.00
PROMISED_UP = 50.00

# * Create a class name
class InternetSpeedBot:
    
    # CONSTRUCTOR for the class
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    # * Methods must contain self in the attributes to be used with variables in the constructor
    def get_internetSpeed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        cookie = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookie.click()
        
        start_test = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_test.click()
        
        time.sleep(50)
        
        download_speed =  self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = float(download_speed)
        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = float(upload_speed)
        
    
    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        time.sleep(5)
        login = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div/span/span')
        login.click()
        time.sleep(4)
        username = self.driver.find_element(By.NAME, value='text')
        username.send_keys(os.environ['EMAIL'], Keys.ENTER)
        time.sleep(3)
        try:
            
            password = self.driver.find_element(By.NAME, value='password')
            password.send_keys(os.environ['PASSWORD'], Keys.ENTER)
            time.sleep(5)
        except NoSuchElementException:
            user = self.driver.find_element(By.NAME, value="text")
            user.send_keys(os.environ['USERNAME'], Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.NAME, value='password')
            password.send_keys(os.environ['PASSWORD'], Keys.ENTER)
            time.sleep(5)
        input_field = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div')
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            tweet = f"Hey @vodafone my rated internet speed should be 500mbps and upload 100mbps\nThe speed I am getting is \n{self.down} download and {self.up} upload \n Plz fix"
            input_field.send_keys(tweet)
    
bot = InternetSpeedBot()
bot.get_internetSpeed()
bot.tweet_at_provider()

input("Press to close the browser")
bot.driver.quit()