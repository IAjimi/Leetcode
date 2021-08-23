class Solution:
	def isValidSudoku(self, board):
		"""
		Runtime: 88 ms, faster than 95.70% of Python3 online submissions for Valid Sudoku.
		Memory Usage: 14.4 MB, less than 16.52% of Python3 online submissions for Valid Sudoku.
		"""
		# Check every row for duplicates
		for ix in range(len(board)):
			row = [b for b in board[ix] if b.isdigit()]
			if len(row) != len(set(row)):
				return False

		# Check every column for duplicates
		for jx in range(9):
			col = [board[ix][jx] for ix in range(9) if board[ix][jx].isdigit()]
			if len(col) != len(set(col)):
				return False

		# Check 3x3 area for duplicates
		for i in (0, 3, 6):
			for j in (0, 3, 6):
				square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y].isdigit()]
				if len(square) != len(set(square)):
					return False

		return True

if __name__ == '__main__':
	board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
		, ["6", ".", ".", "1", "9", "5", ".", ".", "."]
		, [".", "9", "8", ".", ".", ".", ".", "6", "."]
		, ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
		, ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
		, ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
		, [".", "6", ".", ".", ".", ".", "2", "8", "."]
		, [".", ".", ".", "4", "1", "9", ".", ".", "5"]
		, [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

	assert Solution().isValidSudoku(board)