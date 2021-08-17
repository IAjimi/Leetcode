def cum_sum(nums):
	cum_sum = nums[:]
	for ix in range(1, len(cum_sum)):
		cum_sum[ix] += cum_sum[ix - 1]
	return cum_sum


class NumMatrix:
	"""
	Works but is slow. Better approach creates cumulative sum matrix and finds the
	intersection of 4 0-indexed rectangles.

	Runtime: 2884 ms, faster than 5.24% of Python3 online submissions for Range Sum Query 2D - Immutable.
	Memory Usage: 24.2 MB, less than 70.80% of Python3 online submissions for Range Sum Query 2D - Immutable.
	"""
	def __init__(self, matrix):
		self.matrix = [cum_sum(row) for row in matrix]

	def sumRange(self, cum_sum, left, right):
		return cum_sum[right] - cum_sum[left - 1] if left - 1 >= 0 else cum_sum[right]

	def sumRegion(self, row1, col1, row2, col2):
		_sum = 0
		for row in range(row1, row2 + 1):
			_sum += self.sumRange(self.matrix[row], col1, col2)
		return _sum
