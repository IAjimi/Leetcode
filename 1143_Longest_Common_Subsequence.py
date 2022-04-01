class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Runtime: 510 ms, faster than 67.53% of Python3 online submissions for Longest Common Subsequence.
        Memory Usage: 22.7 MB, less than 57.74% of Python3 online submissions for Longest Common Subsequence.
        """
        if len(text1) > len(text2):
            return self.longestCommonSubsequence(text2, text1)

        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
