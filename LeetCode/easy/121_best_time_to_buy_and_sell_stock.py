# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price, max_profit = prices[0], 0
        for v in prices[1:]:
            min_price = min(min_price, v)
            max_profit = max(max_profit, v - min_price)

        return max_profit