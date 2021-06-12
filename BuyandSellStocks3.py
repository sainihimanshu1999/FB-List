'''
it is similar to the normal question, but in this we can do at most two transactions
'''

def stocks(prices):
    min_price = float('inf')
    max_profit = 0
    profits = []

    for price in prices:
        min_price = min(min_price,price)
        profit = price-min_price
        max_profit = max(max_profit,profit)
        profits.append(profit)

    total = 0
    max_profit = 0
    max_price = float('-inf')

    for i in range(len(prices))[::-1]:
        max_price = max(max_price,prices[i])
        profit = max_price-prices[i]
        max_profit =max(profit,max_profit)
        total = max(total,max_profit+profits[i])
    return total

prices = [3,3,5,0,0,3,1,4]
print(stocks(prices))