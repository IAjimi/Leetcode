from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Runtime: 204 ms, faster than 50.30% of Python3 online submissions for Minimum Falling Path Sum.
        Memory Usage: 14.7 MB, less than 79.35% of Python3 online submissions for Minimum Falling Path Sum.
        """
        prev_row = matrix[0]

        for i in range(1, len(matrix)):
            cur_row = []

            for j in range(len(matrix[i])):
                neighbors = [j - 1, j, j + 1]
                cur_sum = min(
                    [prev_row[n] for n in neighbors if 0 <= n <= len(matrix[i]) - 1]
                )
                cur_row.append(cur_sum + matrix[i][j])

            prev_row = cur_row  # update row

        return min(prev_row)
