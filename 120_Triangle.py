from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Runtime: 125 ms, faster than 18.37% of Python3 online submissions for Triangle.
        Memory Usage: 15 MB, less than 75.91% of Python3 online submissions for Triangle.
        """
        n = len(triangle)
        prev_row = triangle[0]

        for i in range(1, n):
            new_row = []
            for j in range(len(triangle[i])):
                prev_step = [j - 1, j]
                min_step = [
                    prev_row[k] for k in prev_step if 0 <= k <= len(triangle[i - 1]) - 1
                ]
                new_row.append(min(min_step) + triangle[i][j])

            prev_row = new_row

        return min(prev_row)
