from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Runtime: 61 ms, faster than 12.07% of Python3 online submissions for Pascal's Triangle II.
        Memory Usage: 13.9 MB, less than 52.06% of Python3 online submissions for Pascal's Triangle II.
        """
        prevRow = [1]

        for n in range(1, rowIndex + 1):
            newRow = [prevRow[i] + prevRow[i + 1] for i in range(len(prevRow) - 1)]
            newRow = [1] + newRow + [1]
            prevRow = newRow

        return prevRow
