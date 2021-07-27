class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		"""
		Runtime: 32 ms, faster than 60.19% of Python3 online submissions.
		Memory Usage: 14 MB, less than 94.62% of Python3 online submissions.
		"""
		pascal_triangle = [[1], [1, 1], [1, 2, 1]]

		if numRows <= 3:
			return pascal_triangle[:numRows]
		else:
			for row in range(4, numRows + 1):
				current_row = []

				for ix in range(row):
					if ix == 0:  # 1st element
						current_row.append(1)
					elif ix == row - 1:  # last element
						current_row.append(1)
					else:
						new_val = pascal_triangle[-1][ix - 1] + pascal_triangle[-1][ix]
						current_row.append(new_val)

				pascal_triangle.append(current_row)

			return pascal_triangle

