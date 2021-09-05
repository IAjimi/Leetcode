class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		"""
		Runtime: 144 ms, faster than 99.89% of Python3 online submissions.
		Memory Usage: 20.6 MB, less than 72.13% of Python3 online submissions.
		"""
		# Sanity check: is target within the range of numbers in this matrix?
		if target > matrix[-1][-1]:
			return False

		row_num = 0

		while row_num < len(matrix):
			row = matrix[row_num]

			# Since we are going row by row, if smallest element of latest row bigger than target
			# target is not in matrix
			if row[0] > target:
				return False
			elif row[-1] < target:
				row_num += 1
			elif row[0] == target or row[-1] == target:
				return True
			else:
				# Run binary search on row
				left, right = 0, len(row) - 1

				while left < right - 1:
					mid = (left + right) // 2

					if row[mid] == target:
						return True
					elif row[mid] < target:
						left = mid
					else:
						right = mid

			row_num += 1

		return False

if __name__ == '__main__':
	assert Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
	assert not Solution().searchMatrix(
		[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 35)
	assert Solution().searchMatrix([[-5]], -5)
	assert Solution().searchMatrix([[-5, 3]], 3)
