import requests
from bs4 import BeautifulSoup
import pprint
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.co.uk/gp/product/B09SWRYPB2/ref=ox_sc_saved_title_6?smid=A3P5ROKL5A1OLE&psc=1"

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.content,"html.parser")

price_output = soup.find("span", class_="a-price-whole").getText()

price = float(price_output.split(".")[0])

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "C00288136@setu.ie"
TO_EMAIL = "michalkuras84@gmail.com"
# PASSWORD = os.environ["EMAILPASSWORD"]

MESSAGE = """Subject: Test Mail for amazon price alert
Hi, This is a test email for a price alert

Thanks
Test"""

smtp = smtplib.SMTP(HOST,PORT)

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Login connection: {status_code} {response}")

smtp.sendmail(FROM_EMAIL,TO_EMAIL,MESSAGE)
smtp.quit


