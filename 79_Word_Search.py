class Solution:
	def exist(self, board, word):
		"""
		Runtime: 6864 ms, faster than 24.29% of Python3 online submissions for Word Search.
		Memory Usage: 14.6 MB, less than 12.97% of Python3 online submissions for Word Search.
		"""
		n = len(board)
		m = len(board[0])

		if len(word) > n * m:
			return False

		# Create lookup table
		dictionary = {}
		for ix in range(n):
			for jx in range(m):
				letter = board[ix][jx]

				if letter in dictionary:
					dictionary[letter].append((ix, jx))
				else:
					dictionary[letter] = [(ix, jx)]

		# Start search
		if word[0] in dictionary:
			queue = [(0, pos, set()) for pos in dictionary[word[0]]]

			while queue:
				n, pos, visited = queue.pop()
				visited.add(pos)

				# Found word
				if n == len(word) - 1:
					return True

				# Keep moving
				neighbors = {(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)}

				next_letter = word[n + 1]
				if next_letter in dictionary:
					for next_pos in dictionary[next_letter]:
						if next_pos in neighbors and next_pos not in visited:
							queue.append((n + 1, next_pos, visited.copy()))

		return False

if __name__ == '__main__':
	assert Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
	assert not Solution().exist(board=[["A", "B"], ["A", "B"]], word="ABCCED")
	assert not Solution().exist(board=[["A", "B", "C"], ["C", "B", "A"]], word="ACBC")
	assert Solution().exist(board=[["A", "B", "C"], ["C", "B", "A"]], word="ACBA")
	assert not Solution().exist(board=[["A", "B", "C"], ["C", "B", "A"]], word="ABCBABCBA")
	assert not Solution().exist(board=[["A", "B", "C"], ["C", "B", "A"]], word="D")
	assert not Solution().exist(board=[["A", "B", "C"], ["C", "B", "A"]], word="ABD")
	assert Solution().exist(board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word="ABCESEEEFS")

