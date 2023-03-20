
# # Extracting Stock information suing API

import pandas as pd
import requests
import json
import yfinance as yf
from datetime import datetime
amd = yf.Ticker("AMD")
print(amd)

# Extracting Stock information using API
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=AMD&apikey=4ZETGE55VA5222S1'
r = requests.get(url)
data = r.json()
print(data)

# Checking the sector of the stock from JSON data
print(data['Sector'])

# Extracting history of the stock from the period it started
amd_share_price_data = amd.history(period="max")
print(amd_share_price_data.iloc[0][4])


#  Extracting the stock information using Beautiful soup

import pandas as pd
import requests
from bs4 import BeautifulSoup
url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data  = requests.get(url).text
print(data)
soup = BeautifulSoup(data, 'html5lib')
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True) 

print(amazon_data.head())
print(amazon_data.tail())


