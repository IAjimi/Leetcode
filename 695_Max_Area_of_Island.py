from typing import List, Tuple


class Solution:
    def bfs(self, start: Tuple[int, int], grid: List[List[int]]):
        size = 0
        q = [start]

        while q:
            i, j = q.pop()

            if not (0 <= i <= len(grid) - 1) or not (0 <= j <= len(grid[0]) - 1):
                continue
            elif grid[i][j] != 1:
                continue

            grid[i][j] = 0  # mark as visited
            size += 1
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for n in neighbors:
                q.append(n)

        return grid, size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Runtime: 156 ms, faster than 77.60% of Python3 online submissions for Max Area of Island.
        Memory Usage: 14.9 MB, less than 73.57% of Python3 online submissions for Max Area of Island.
        """
        max_size = 0
        ones = [
            (i, j)
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == 1
        ]

        while ones:
            start = ones.pop()
            if grid[start[0]][start[1]] == 1:
                grid, size = self.bfs(start, grid)
                max_size = max(max_size, size)

        return max_size
