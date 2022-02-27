from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Runtime: 1080 ms, faster than 81.32% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 25 MB, less than 65.03% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        local_min = 10**5
        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < local_min:
                local_min = prices[i]

            profit = max(profit, prices[i + 1] - local_min)

        return profit


def test_maxProfit():
    assert 0 == Solution().maxProfit([0])
    assert 1 == Solution().maxProfit([0, 1])
    assert 0 == Solution().maxProfit([1, 0])
    assert 2 == Solution().maxProfit([0, 1, 2])
    assert 2 == Solution().maxProfit([1, 0, 2])
    assert 2 == Solution().maxProfit([2, 4, 1])
    assert 3 == Solution().maxProfit([4, 7, 1, 2])
    assert 5 == Solution().maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == Solution().maxProfit([7, 6, 4, 3, 1])
