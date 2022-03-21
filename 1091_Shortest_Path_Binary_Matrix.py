from typing import List
from heapq import heappop, heappush


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Runtime: 2075 ms, faster than 5.01% of Python3 online submissions for Shortest Path in Binary Matrix.
        Memory Usage: 14.4 MB, less than 67.99% of Python3 online submissions for Shortest Path in Binary Matrix.
        """
        q = [(1, (0, 0))]

        while q:
            steps, (i, j) = heappop(q)

            if not (0 <= i <= len(grid) - 1) or not (0 <= j <= len(grid) - 1):
                continue
            elif grid[i][j] != 0:
                continue

            grid[i][
                j
            ] = 1  # mark as visited - could also use set if do not want to change grid

            if i == len(grid) - 1 and j == len(grid) - 1:
                return steps

            neighbors = [
                (i - 1, j),
                (i + 1, j),
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j + 1),
                (i, j - 1),
                (i, j + 1),
            ]
            for n in neighbors:
                heappush(q, (steps + 1, n))

        return -1
