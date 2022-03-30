from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Runtime: 280 ms, faster than 99.68% of Python3 online submissions for Minimum Falling Path Sum II.
        Memory Usage: 17.3 MB, less than 68.47% of Python3 online submissions for Minimum Falling Path Sum II.
        """
        n = len(matrix)
        m = len(matrix[0])

        if m == 1:
            return matrix[0][0]

        prev_row = [0 for _ in range(m)]

        for i in range(n):
            cur_row = []
            min1 = min(prev_row)
            min1_ix = prev_row.index(min1)
            min2 = min(prev_row[:min1_ix] + prev_row[min1_ix + 1 :])

            for j in range(m):
                prev_min = min1 if min1_ix != j else min2
                cur_row.append(prev_min + matrix[i][j])

            prev_row = cur_row  # update row

        return min(prev_row)
