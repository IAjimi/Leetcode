from typing import List

from heapq import heappop, heappush


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Runtime: 64 ms, faster than 67.69% of Python3 online submissions for Rotting Oranges.
        Memory Usage: 14 MB, less than 51.32% of Python3 online submissions for Rotting Oranges.
        """
        # Create constants
        n = len(grid)
        m = len(grid[0])
        n_oranges = sum([1 for i in range(n) for j in range(m) if grid[i][j] != 0])

        # Edge case
        if n_oranges == 0:
            return 0

        # Use BFS to count number of turns needed to turn all oranges
        turn = 0
        q = []
        rotten = set()

        # Add rotten oranges to queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    heappush(q, (0, (i, j)))

        # BFS from queue
        while q:
            turn, (i, j) = heappop(q)

            if (i, j) in rotten:
                continue
            elif not (0 <= i <= n - 1) or not (0 <= j <= m - 1):
                continue
            elif grid[i][j] == 0:
                continue

            rotten.add((i, j))

            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for nn in neighbors:
                heappush(q, (turn + 1, nn))

        if len(rotten) == n_oranges:
            return turn - 1
        else:
            return -1
