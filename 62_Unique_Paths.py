class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Runtime: 39 ms, faster than 67.02% of Python3 online submissions for Unique Paths.
        Memory Usage: 13.9 MB, less than 42.53% of Python3 online submissions for Unique Paths.
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row != 0 and col != 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
