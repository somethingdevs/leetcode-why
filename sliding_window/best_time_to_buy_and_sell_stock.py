from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price, max_profit = prices[0], 0

    if len(prices) == 1:
        return 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
