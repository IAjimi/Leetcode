from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Runtime: 104 ms, faster than 86.37% of Python3 online submissions for Minimum Path Sum.
        Memory Usage: 14.7 MB, less than 94.02% of Python3 online submissions for Minimum Path Sum.
        """
        prev_row: List[int] = [0 for j in grid[0]]

        for i in range(len(grid)):
            cur_row = []

            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    val = grid[i][j]
                elif i == 0:
                    val = cur_row[-1] + grid[i][j]
                elif j == 0:
                    val = prev_row[j] + grid[i][j]
                else:
                    val = min(prev_row[j], cur_row[-1]) + grid[i][j]

                cur_row.append(val)

            prev_row = cur_row

        return prev_row[-1]
