import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Enter a ticker: ")
print(stock)
start_year = input("Enter a start year: ")
print(start_year)
start_month = input("Enter a start month: ")
print(start_month)
start_day = input("Enter a start day: ")
print(start_day)


start = dt.datetime(int(start_year), int(start_month), int(start_day))
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

## begin@

exp_mv_avg = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]

for x in exp_mv_avg:
    df["Ema_" + str(x)] = round(df.iloc[:,4].ewm(span=x, adjust=False).mean(), 2)

print(df.tail())

for i in df.index:
    c_min = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i], df["Ema_30"][i],df["Ema_45"][i],df["Ema_50"][i],df["Ema_60"][i])
    c_max = max(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i], df["Ema_30"][i],df["Ema_45"][i],df["Ema_50"][i],df["Ema_60"][i])

    close = df["Adj Close"][i]

    if c_min > c_max:
        print("Red White Blue")
    elif c_min < c_max:
        print("Blue White Red")







## begin@
# moving_avg = 50
#
# sma_string = "SMA_" + str(moving_avg)
#
# df[sma_string] = df.iloc[:,4].rolling(window=moving_avg).mean()
#
# df = df.iloc[moving_avg:]
#
# print(df)
#
#
# num_h = 0
# num_c = 0
# for i in df.index:
#     if df["Adj Close"][i] > df[sma_string][i]:
#         print("The close: {} is higher than the {}: {}. ".format(df["Adj Close"][i], sma_string, df[sma_string][i]))
#         num_h += 1
#     else:
#         print("The close is lower than the {}".format(sma_string))
#         num_c += 1
# print(num_h)
# print(num_c)