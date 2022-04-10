from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Runtime: 124 ms, faster than 90.26% of Python3 online submissions.
        Memory Usage: 15.2 MB, less than 14.29% of Python3 online submissions.

        Do not return anything, modify matrix in-place instead.

        Test case:
        * [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]
        * [[0,1,2,0],[3,4,5,2],[1,3,1,5]] -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        * [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]] -> [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        * [[1],[0],[3]] -> [[0],[0],[0]]
        """
        # Check for 0 in first row
        first_row_zero = True if 0 in matrix[0] else False
        first_col_zero = (
            True if 0 in [matrix[ix][0] for ix in range(len(matrix))] else False
        )

        # Iterate over matrix to find 0s
        for ix in range(len(matrix)):
            row = matrix[ix]
            for jx in range(len(row)):
                if row[jx] == 0:
                    row[0] = 0  # set 1st cell of the row to 0
                    matrix[0][jx] = 0  # set 1st cell of the column to 0

        # Iterate over first row (avoid first column)
        for ix in range(1, len(matrix)):
            if matrix[ix][0] == 0:
                matrix[ix] = [0 for _ in matrix[ix]]

        # Iterate over first column (avoid first row)
        for jx in range(1, len(matrix[0])):
            if matrix[0][jx] == 0:
                for ix in range(len(matrix)):
                    matrix[ix][jx] = 0

        # Finally check matrix[0][0] (the original version - flags make this complicated)
        if first_row_zero:
            matrix[0] = [0 for _ in range(len(matrix[0]))]  # 1st row

        if first_col_zero:
            for jx in range(len(matrix)):
                matrix[jx][0] = 0  # 1st element of every row
