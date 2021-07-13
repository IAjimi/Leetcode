class Solution:
	def arraySign(self, nums: List[int]) -> int:
		"""
		Runtime: 60 ms, faster than 67.44% of Python3 online submissions.
		Memory Usage: 14.5 MB, less than 34.84% of Python3 online submissions.
		"""
		if 0 in nums:
			return 0

		sign = [1 if n < 0 else 0 for n in nums]

		if sum(sign) % 2 == 0:
			return 1
		else:
			return -1