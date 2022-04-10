class Solution:
    def spiralOrder(self, matrix):
        """
        Runtime: 32 ms, faster than 58.24% of Python3 online submissions.
        Memory Usage: 14.3 MB, less than 59.43% of Python3 online submissions.
        """
        min_row, max_row = 0, len(matrix) - 1
        min_col, max_col = 0, len(matrix[0]) - 1

        solution = []

        while min_col < max_col and min_row < max_row:
            solution += [
                matrix[min_row][col] for col in range(min_col, max_col)
            ]  # right
            solution += [
                matrix[row][max_col] for row in range(min_row, max_row)
            ]  # down
            solution += [
                matrix[max_row][col] for col in range(max_col, min_col, -1)
            ]  # left
            solution += [
                matrix[row][min_col] for row in range(max_row, min_row, -1)
            ]  # up
            min_row += 1
            max_col += -1
            max_row += -1
            min_col += 1

        if min_row == max_row and min_col == max_col:
            solution.append(matrix[min_row][min_col])
        elif min_row < max_row and min_col == max_col:
            for row in range(min_row, max_row + 1):
                solution.append(matrix[row][min_col])
        elif min_col < max_col and min_row == max_row:
            for col in range(min_col, max_col + 1):
                solution.append(matrix[min_row][col])

        return solution


if __name__ == "__main__":
    assert [1, 2, 3] == Solution().spiralOrder(matrix=[[1, 2, 3]])
    assert [3, 2] == Solution().spiralOrder(matrix=[[3, 2]])
    assert [3, 2, 4, 5] == Solution().spiralOrder(matrix=[[3], [2], [4], [5]])
    assert [1, 2, 3, 6, 5, 4] == Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6]])
    assert [1, 2, 4, 6, 5, 3] == Solution().spiralOrder(matrix=[[1, 2], [3, 4], [5, 6]])
    assert [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == Solution().spiralOrder(
        matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    )
    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == Solution().spiralOrder(
        matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
    assert [2, 3, 4, 7, 10, 13, 12, 11, 8, 5, 6, 9] == Solution().spiralOrder(
        matrix=[[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]
    )
