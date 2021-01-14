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

pos = 0 # to determine if we are entered into a position, entered = 1, not = 0
num = 0 # keep track of row on
percent_change = [] # add results of trades

for i in df.index:
    c_min = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i])
    c_max = max(df["Ema_30"][i],df["Ema_35"][i],df["Ema_40"][i],df["Ema_45"][i],df["Ema_50"][i],df["Ema_60"][i])

    close = df["Adj Close"][i]

    if c_min > c_max:
        print("Red White Blue")
        if pos == 0:
            buy_price = close
            pos = 1
            print("Buying now at " + str(buy_price))
    elif c_min < c_max:
        print("Blue White Red")
        if pos == 1:
            pos = 0
            sell_price = close
            print("selling now at " + str(sell_price))
            pc = (sell_price/buy_price - 1) * 100
            percent_change.append(pc)
    # if at end of pandas df and still have position open
    if num == df["Adj Close"].count()-1 and pos == 1:
        pos = 0
        sell_price = close
        print("selling now at " + str(sell_price))
        pc = (sell_price / buy_price - 1) * 100
        percent_change.append(pc)
    num += 1

print(percent_change)

gains = 0
num_gains = 0
losses = 0
num_losses = 0
total_return = 1

for i in percent_change:
    if i > 0:
        gains += i
        num_gains += 1
    else:
        losses += i
        num_losses += 1
    total_return = total_return * ((i/100) + 1)

total_return = round((total_return - 1) * 100, 2)

if num_gains > 0:
    avg_gain = gains / num_gains
    max_ret = str(max(percent_change))
else:
    avg_gain = 0
    max_ret = "undefined"

if num_losses > 0:
    avg_loss = losses / num_losses
    max_loss = str(min(percent_change))
    ratio = str(-avg_gain / avg_loss)
else:
    avg_loss = 0
    max_loss = "undefined"
    ratio = "inf"

if num_gains > 0 or num_losses > 0:
    batting_avg = num_gains / (num_gains + num_losses)
else:
    batting_avg = 0


print("===========================")
print()
print("Results for "+ stock +" going back to "+str(df.index[0])+", Sample size: "+str(num_gains+num_losses)+" trades")
print("EMAs used: "+str(exp_mv_avg))
print("Batting Avg: "+ str(batting_avg))
print("Gain/loss ratio: "+ ratio)
print("Average Gain: "+ str(avg_gain))
print("Average Loss: "+ str(avg_loss))
print("Max Return: "+ max_ret)
print("Max Loss: "+ max_loss)
print("Total return over "+str(num_gains + num_losses)+ " trades: "+ str(total_return)+"%" )
#print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )
print()


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