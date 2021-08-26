import numpy as np


class Solution:
	def judgeSquareSum(self, c: int) -> bool:
		"""
		Runtime: 376 ms, faster than 29.30% of Python3 online submissions.
		Memory Usage: 34.8 MB, less than 5.47% of Python3 online submissions.
		"""
		sq_root = np.sqrt(c)

		if sq_root.is_integer():
			return True
		else:
			nums = {n ** 2 for n in range(int(sq_root) + 1)}

			for n in nums:
				target = c - n
				if target in nums:
					return True

			return False

	def oldJudgeSquareSum(self, c: int) -> bool:
		"""
		Runtime: 684 ms, faster than 10.60% of Python3 online submissions.
		Memory Usage: 30.7 MB, less than 5.47% of Python3 online submissions.
		"""
		sq_root = np.sqrt(c)

		if sq_root.is_integer():
			return True
		else:
			for n in range(int(sq_root) + 1):
				target = c - n ** 2
				if (np.sqrt(target)).is_integer():
					return True

			return False


