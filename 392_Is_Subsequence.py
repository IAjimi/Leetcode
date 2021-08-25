class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		"""
		Runtime: 84 ms, faster than 6.64% of Python3 online submissions.
		Memory Usage: 14.9 MB, less than 9.72% of Python3 online submissions.

		Using similar method to 1143 Longest Common Subsequence with early termination if
		s isn't a subsequence.

		Creating a dp matrix, where dp[i][j] is the length of subsequence s[:i] in t[:j].
		The value at dp[i+1][j+1] is the maximum of
			* the length of the subsequence s[:i] in t[:j+1]
			(i.e., the length of the subsequence without this new letter)
			+ 1 if s[i+1] == t[j+1]
			AND
			* the length of the subsequence s[:i+1] in t[:j] (length of the subsequence with
			letter s[i+1] included)
		"""
		# For clarity, creating len() vars
		substr_len = len(s)
		str_len = len(t)

		# Checking for edge cases
		if substr_len > str_len:
			return False
		if substr_len == 0:
			return True

		# Start dp
		dp = [[0] * str_len for _ in range(substr_len)]

		for i in range(substr_len):
			for j in range(i, str_len):
				is_match = 1 * (s[i] == t[j])
				dp[i][j] = max(dp[i - 1][j - 1] + is_match, dp[i][j - 1])

			# Current s[i] wasn't a match, so s isn't a subsequence of t
			if dp[i][-1] < i + 1:
				return False

		return True
