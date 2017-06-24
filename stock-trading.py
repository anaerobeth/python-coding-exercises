"""
Calculate the best profit made from one purchase and one sale of
a stock within the same trading day
"""

def get_max_profit(stock_prices):
    buy, sell = 0, 0
    max_profit = 0

    if not stock_prices:
        pass
    else:
        min_price = stock_prices[0]

        # loop through prices
        for current_price in stock_prices:

            # is this the lowest price seen?
            min_price = min(min_price, current_price)
            profit = current_price - min_price

            # update profit if we can do better
            if profit > max_profit:
                max_profit = profit
                buy, sell = min_price, current_price

    if buy == sell:
        return 'No trade is possible today'
    else:
        return (max_profit, buy, sell)


assert get_max_profit([]) == 'No trade is possible today'
assert get_max_profit([1, 1, 1, 1, 1]) == 'No trade is possible today'

sample = [10, 7, 5, 8, 11, 9, 4]
assert get_max_profit(sample) == (6, 5, 11)
max_profit, buy, sell = get_max_profit(sample)
print("Buy at ${} and sell at ${} for a profit of ${}".format(buy, sell, max_profit))

