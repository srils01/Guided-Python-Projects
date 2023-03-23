

import pandas as pd
import requests
import json
import yfinance as yf
from datetime import datetime
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Extracting Stock information of Tesla using yfinance

tesla = yf.Ticker("TSLA")
print(tesla)
tesla_data=tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))

 # Extracting Stock information of Tesla using webscraping

url="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response= requests.get(url)
html_data=response.text
soup = BeautifulSoup(html_data,"html.parser")
print(soup.title)

tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup.find_all("tbody")[1].find_all("tr"):
    columns = row.find_all("td")
    date = columns[0].text
    revenue = columns[1].text
    tesla_revenue=tesla_revenue.append({'Revenue':revenue,'Date':date},ignore_index=True)
    tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"")
    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    print(tesla_revenue.tail(5))


# Extracting Stock information of GME using yfinance

gme = yf.Ticker("GME")
gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head(5))


# # Extracting stock data of GME using webscraping   
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response=requests.get(url)
html_data=response.text
soup = BeautifulSoup(html_data,"html.parser")
print(soup.title.text)

gme_revenue= pd.DataFrame(columns=['Date', 'Revenue'])
# print(soup.find_all("tbody")[1].find_all("tr"))
for row in soup.find_all("tbody")[1].find_all("tr"):
    columns = row.find_all("td")
    revenue = columns[1].text
    print(revenue)
    date = columns[0].text
    print(date)   
    gme_revenue=gme_revenue.append({'Revenue':revenue,'Date':date},ignore_index=True)
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$',"")
    gme_revenue.dropna(inplace=True)
    gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
    print(gme_revenue.tail(5))

# # Tesla Stock Graph
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title="Tesla Stock Graph",
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph(tesla_data,tesla_revenue,tesla)

# # GME stock graph
def make_graph_gme(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title="GME Stock Graph",
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph_gme(gme_data,gme_revenue,gme)
