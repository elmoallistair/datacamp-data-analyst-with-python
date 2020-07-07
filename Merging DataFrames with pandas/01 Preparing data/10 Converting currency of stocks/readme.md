## Converting currency of stocks

In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from [Yahoo Finance](https://finance.yahoo.com/). The files `sp500.csv` for sp500 and `exchange.csv` for the exchange rates are both provided to you.

Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.

<hr>

**Instructions**
* Read the DataFrames `sp500` & `exchange` from the files `'sp500.csv'` & `'exchange.csv'` respectively..
* Use `parse_dates=True` and `index_col='Date'`.
* Extract the columns `'Open'` & `'Close'` from the DataFrame `sp500` as a new DataFrame `dollars` and print the first 5 rows.
* Construct a new DataFrame `pounds` by converting US dollars to British pounds. You'll use the `.multiply()` method of `dollars` with `exchange['GBP/USD']` and `axis='rows'`
* Print the first 5 rows of the new DataFrame `pounds`. This has been done for you, so hit 'Submit Answer' to see the results!.

## Script
```
# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv',index_col='Date',parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv',index_col='Date',parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open','Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

# Print the head of pounds
print(pounds.head())
```

## Output
```
<script.py> output:
                       Open        Close
    Date
    2015-01-02  2058.899902  2058.199951
    2015-01-05  2054.439941  2020.579956
    2015-01-06  2022.150024  2002.609985
    2015-01-07  2005.550049  2025.900024
    2015-01-08  2030.609985  2062.139893
                       Open        Close
    Date
    2015-01-02  1340.364425  1339.908750
    2015-01-05  1348.616555  1326.389506
    2015-01-06  1332.515980  1319.639876
    2015-01-07  1330.562125  1344.063112
    2015-01-08  1343.268811  1364.126161
```