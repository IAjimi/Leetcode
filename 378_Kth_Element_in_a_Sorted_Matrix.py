class Solution:
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		"""
		Runtime: 164 ms, faster than 86.92% of Python3 online submissions.
		Memory Usage: 20.2 MB, less than 49.80% of Python3 online submissions.
		"""
		matrix = [item for sublist in matrix for item in sublist]  # in place to limit memory usage
		return sorted(matrix)[k - 1]
