from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        DP approach with one array. Implicitly equivalent to the construction below,
        where dp[i][j] = dp[i - 1][j] + dp[i][j - c] if j - c >= 0 else dp[i - 1][j],
        as dp[i][j] is initially already equal to dp[i - 1][j].

        Runtime: 132 ms, faster than 95.89% of Python3 online submissions.
        Memory Usage: 14.2 MB, less than 95.83% of Python3 online submissions.
        """
        nways = [0] * (amount + 1)
        nways[0] = 1

        for ix, c in enumerate(coins):
            # For values that can be made with current coin, find ways to build remainder
            for n in range(c, amount + 1):
                nways[n] += nways[n - c]

        return nways[-1]

    def oldChange(self, amount: int, coins: List[int]) -> int:
        """
        Runtime: 168 ms, faster than 68.86% of Python3 online submissions.
        Memory Usage: 29.5 MB, less than 38.48% of Python3 online submissions.
        """
        ways_of_making = [[0] * (amount + 1) for c in coins]

        for ix, c in enumerate(coins):
            # Set ways of making 0 to 1
            ways_of_making[ix][0] = 1

            # Set row to previous row (ways of making without current coin)
            if ix > 0:
                ways_of_making[ix] = ways_of_making[ix - 1].copy()

            # For values that can be made with current coin, find ways to build remainder
            for n in range(c, amount + 1):
                ways_of_making[ix][n] += ways_of_making[ix][n - c]

        return ways_of_making[-1][-1]
