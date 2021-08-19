class Solution:
	def lengthOfLongestSubstring(self, string: str) -> int:
		"""
		Runtime: 52 ms, faster than 91.76% of Python3 online submissions.
		Memory Usage: 14.2 MB, less than 80.56% of Python3 online submissions.
		"""
		if len(string) == 0:
			return 0
		else:
			l = 0
			max_length = 0
			substring = {}

			for ix in range(len(string)):
				s = string[ix]
				if s not in substring:
					substring[s] = ix
					max_length = max(ix - l + 1, max_length)
				else:
					if l <= substring[s]:
						l = substring[s] + 1
					else:
						max_length = max(ix - l + 1, max_length)
					substring[s] = ix

			return max_length

if __name__ == '__main__':
	assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
	assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
	assert 3 == Solution().lengthOfLongestSubstring("pwwkew")
	assert 0 == Solution().lengthOfLongestSubstring("")
	assert 5 == Solution().lengthOfLongestSubstring("tmmzuxt")
	assert 4 == Solution().lengthOfLongestSubstring("aaaabcda")
