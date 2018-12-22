"""
Risk Analysis of FANG stock prices using Monte Carlo simulation

Adapted from https://www.analyticsindiamag.com/a-primer-to-monte-carlo-simulation-in-python/
"""

import matplotlib
import numpy as np
import pandas
from scipy.stats import norm

# Workaround for MacOS/conda setup
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import quandl

stocks = ['FB', 'AMZN', 'NFLX','GOOG']

def forecast(stock):
    tracker = 'WIKI/{}'.format(stock)
    filename = '{}_forecast.png'
    data = quandl.get(tracker, start_date='2006-01-01', end_date='2018-12-1')['Adj. Close']

    log_returns = np.log(1 + data.pct_change())
    u = log_returns.mean()
    var = log_returns.var()
    stdev = log_returns.std()
    drift = u - (0.5 * var)

    # Forecast future stock prices for every trading day a year ahead
    t_intervals = 252
    iterations = 10

    Z = norm.ppf(np.random.rand(t_intervals, iterations))
    daily_returns = np.exp(drift + stdev * Z)

    last_closing_price = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = last_closing_price

    # Reassign price to the product of daily returns and the previous closing 
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]

    plt.figure(figsize=(10,5))
    plt.plot(price_list)
    plt.title(stock)
    plt.xlabel('Day')
    plt.ylabel('Forecast Price')
    plt.savefig(filename)

for stock in stocks:
    print('Generating forecast for {}'.format(stock))
    forecast(stock)
    print('DONE')
