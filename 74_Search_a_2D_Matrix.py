from typing import List


class Solution:
    def binarySearch(
        self, matrix: List[List[int]], target: int, row: int, left: int, right: int
    ) -> bool:
        if right < left:
            return False

        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        return self.binarySearch(matrix, target, row, left, right)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. Do modified binary search to find proper row
        2. Do binary search on row to find target

        Runtime: 68 ms, faster than 41.79% of Python3 online submissions for Search a 2D Matrix.
        Memory Usage: 14.5 MB, less than 38.96% of Python3 online submissions for Search a 2D Matrix.
        """
        left = 0
        right = len(matrix) - 1

        while 0 <= left <= right <= len(matrix) - 1:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binarySearch(matrix, target, mid, 0, len(matrix[mid]) - 1)
            elif matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1

        return False
