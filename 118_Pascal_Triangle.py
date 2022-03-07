from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Runtime: 40 ms, faster than 61.87% of Python3 online submissions for Pascal's Triangle.
        Memory Usage: 13.9 MB, less than 52.79% of Python3 online submissions for Pascal's Triangle.
        """
        rows = [[1]]

        for n in range(1, numRows):
            newRow = [
                rows[n - 1][i] + rows[n - 1][i + 1] for i in range(len(rows[n - 1]) - 1)
            ]
            newRow = [1] + newRow + [1]
            rows.append(newRow)

        return rows
