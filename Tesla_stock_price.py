

import requests

parameters={

"function":"TIME_SERIES_DAILY_ADJUSTED",
"symbol":"TSLA",
"apikey":"GNSRTNBY9YRFOODL"


}

response=requests.get("https://www.alphavantage.co/query",params=parameters)
data = response.json()["Time Series (Daily)"]
print(response.json())
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
print(difference)

percentage_difference=(difference/float(yesterday_closing_price))*100
print(percentage_difference)

if percentage_difference>3:
    print("get news")

news_params={
    "apiKey":"cbeba3d2e3a84f49a08194f38a6f3e6e",
    "q":"Tesla Inc",
}

news_response=requests.get("https://newsapi.org/v2/everything",news_params)
articles=news_response.json()["articles"]

three_articles=articles[:3]
print(three_articles)

