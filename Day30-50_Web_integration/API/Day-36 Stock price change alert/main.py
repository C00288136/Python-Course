import requests
import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = os.environ["STOCK_API"]

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : STOCK_API
}

NEWS_API = os.environ["NEW_API"]
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"




## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_r = requests.get(STOCK_ENDPOINT,params=stock_params)
# print(stock_r.raise_for_status)
data = stock_r.json()
time_series = data["Time Series (Daily)"]
sorted_dates = sorted(time_series.keys(), reverse=True)

# Get the latest and previous dates
latest_date = sorted_dates[0]
previous_date = sorted_dates[1]

# Extract the data for these dates
latest_data = time_series[latest_date]
previous_data = time_series[previous_date]
# Extract just the close data
latest_close = float(latest_data["4. close"])
previous_close = float(previous_data["4. close"])
# Convert change to percent
percentage_change =((latest_close - previous_close) / previous_close) * 100

if percentage_change >= 5:
    new_params = {
    "q" : COMPANY_NAME,
    "apiKey": NEWS_API,
    "language" : "en"

}
    news_r = requests.get(NEWS_ENDPOINT,params=new_params)

    data = news_r.json()
    articles = data["articles"]

    three_articles = articles[:3]

# list comprehension

formatted_articles = [f"{COMPANY_NAME}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n"
                      f"Headline: {article['title']}\n"
                      f"Brief: {article['description']}\n"
                      for article in three_articles]

for article in formatted_articles:
    print(article)
    print("\n")
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=f"{article}",
                        from_='+15014394409',
                        to='+353874442242'
                    )

    print(message.status)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

