from collections import defaultdict
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        Runtime: 3172 ms, faster than 21.44% of Python3 online submissions for Maximum Earnings From Taxi.
        Memory Usage: 44.8 MB, less than 25.00% of Python3 online submissions for Maximum Earnings From Taxi.
        """
        # store rides by end time in hashmap
        rides_dict = defaultdict(list)
        for start, end, tip in rides:
            rides_dict[end].append((start, end - start + tip))

        # find max for every end time
        dp = []

        for i in range(n + 1):
            current_profit = dp[-1] if dp else 0

            for start, new_profit in rides_dict[i]:
                new_profit += dp[start]
                current_profit = max(current_profit, new_profit)

            dp.append(current_profit)

        return dp[-1]
