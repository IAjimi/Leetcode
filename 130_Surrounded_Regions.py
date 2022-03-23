from typing import List


class Solution:
    def dfs(self, board: List[List[str]], start):
        q = [start]
        visited = set()
        at_edge = False

        while q:
            i, j = q.pop()

            if not (0 <= i <= len(board) - 1) or not (0 <= j <= len(board[0]) - 1):
                continue
            elif board[i][j] == "X":
                continue
            elif (i, j) in visited:
                continue

            visited.add((i, j))

            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                at_edge = True

            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for n in neighbors:
                q.append(n)

        return visited, at_edge

    def update_board(self, board, visited, at_edge):
        if at_edge:
            return board

        for (i, j) in visited:
            board[i][j] = "X"

        return board

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Key insight: a region is only not surrounded if it touches one of the edges of the board.

        Runtime: 3451 ms, faster than 5.00% of Python3 online submissions for Surrounded Regions.
        Memory Usage: 26.2 MB, less than 12.27% of Python3 online submissions for Surrounded Regions.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    visited, at_edge = self.dfs(board, (i, j))
                    board = self.update_board(board, visited, at_edge)
