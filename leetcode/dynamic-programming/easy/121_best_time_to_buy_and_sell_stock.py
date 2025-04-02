#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class Solution contains a method to solve the problem of finding the maximum profit
    from a list of stock prices, where you are allowed to complete at most one transaction
    (buy one and sell one share of the stock).

    Methods:
        maxProfit(prices: List[int]) -> int:
            Calculates the maximum profit that can be achieved from the given list of stock prices.
            The input is a list of integers where each element
            represents the stock price on a given day.
            Returns the maximum profit as an integer. If no profit can be made, returns 0.
    """

    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     for i, price in enumerate(prices):
    #         for nextPrice in prices[i:]:
    #             profit = max(profit, nextPrice - price)
    #     return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     left = 0  # Buy
    #     right = 1  # Sell
    #     max_profit = 0
    #     while right < len(prices):
    #         currentProfit = prices[right] - prices[left]  # our current Profit
    #         max_profit = max(currentProfit, max_profit)
    #         if prices[left] > prices[right]:
    #             left = right
    #         right += 1
    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# @lc code=end


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # No profit can be made
        ([1, 2, 3, 4, 5], 4),  # Buy at 1, sell at 5
        ([2, 4, 1], 2),  # Buy at 2, sell at 4
        ([3, 2, 6, 5, 0, 3], 4),  # Buy at 2, sell at 6
    ],
)
def test_max_profit(prices, expected):
    solution = Solution()
    assert solution.maxProfit(prices) == expected
