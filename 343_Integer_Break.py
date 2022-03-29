class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Runtime: 43 ms, faster than 63.88% of Python3 online submissions for Integer Break.
        Memory Usage: 13.9 MB, less than 68.08% of Python3 online submissions for Integer Break.
        """
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1

        for i in range(1, n + 1):
            for j in range(i // 2, i):
                complement = i - j
                max_c = max(complement, dp[complement])
                max_j = max(j, dp[j])
                dp[i] = max(dp[i], max_c * max_j)

        return dp[-1]
