import requests as rq
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = "xxxx"
NEWS_API_KEY = "xxxx"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

url_alpha = STOCK_ENDPOINT
parameters = {
    "symbol": "TSLA",
    "apikey": ALPHA_API_KEY,
    "datatype": "json",
    "function": "TIME_SERIES_DAILY"
}
r = rq.get(url_alpha, params=parameters)
d = r.json()["Time Series (Daily)"]
data_list = [value for (key,value) in d.items()]
    
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_the_yesterday = data_list[1]
day_before_closing_price = day_before_the_yesterday["4. close"]

differ = abs(float(yesterday_closing_price) - float(day_before_closing_price))
plus_differ = (differ / float(yesterday_closing_price)) * 100

print(plus_differ)

if plus_differ > 2:
    url_news = NEWS_ENDPOINT
    parameters= {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = rq.get(url_news,params=parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    
    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]    
    
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            body = article,
            from_ = "+170xxxxxxxxx",
            to = "YOUR_NUMBER",
        )

