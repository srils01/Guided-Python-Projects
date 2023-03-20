import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

amd = yf.Ticker("amd")
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
   
amd_info