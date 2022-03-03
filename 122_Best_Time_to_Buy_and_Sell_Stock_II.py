from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find local min, local max, reset when new local min.

        Runtime: 103 ms, faster than 33.48% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 15.1 MB, less than 50.96% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        """

        profit = 0
        local_max = prices[0]
        local_min = prices[0]

        for i, p in enumerate(prices):
            if p < prices[i - 1]:  # SELL
                profit = max(profit, profit + local_max - local_min)
                local_min = p
                local_max = p
            elif p < local_min:  # BUY
                local_min = p
                local_max = p  # can't carry old max bc buying stock now
            else:
                local_max = max(local_max, p)

        profit += local_max - local_min
        return profit
