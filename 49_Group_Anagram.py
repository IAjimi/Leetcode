class Solution:
	def groupAnagrams(self, strs):
		"""
		Runtime: 145 ms, faster than 13.32% of Python3 online submissions.
		Memory Usage: 17.3 MB, less than 77.13% of Python3 online submissions.
		"""
		d = {}

		for word in strs:
			sorted_word = [w for w in word]
			sorted_word.sort()
			sorted_word = ''.join(sorted_word)

			if sorted_word in d:
				d[sorted_word].append(word)
			else:
				d[sorted_word] = [word]

		return list(d.values())

if __name__ == '__main__':
	Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])