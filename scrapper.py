import yfinance as yf
import pandas as pd
from datetime import date

name = input("ENTER STOCK ID: ")

period = input("ENTER ANALYSIS PERIOD (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max): ")

res = int(input("ENTER NUMBER OF SAMPLES YOU WANT TO ANALYSE: "))

st = yf.Ticker(name)

hist = st.history(period=period)
(a,b) = hist.shape
print(type(a))
top = hist.head()
data_list = []

if res > a:
    for i in hist.index:
        data_list.append(hist.at[(str(i.date())), 'High'])
    print(hist.High)
    print(data_list)

if res < a:
    val = int(a/res)
    g = 0
    for i in hist.index:
        g+=1
        if g == val:
            data_list.append(hist.at[(str(i.date())), 'High'])
            g = 0
    print(val)
    print(data_list)
