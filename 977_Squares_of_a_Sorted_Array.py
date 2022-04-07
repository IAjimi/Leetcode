from typing import List


class Solution:
    def trivialSortedSquares(self, nums: List[int]) -> List[int]:
        """
        Runtime: 220 ms, faster than 92.33% of Python3 online submissions for Squares of a Sorted Array.
        Memory Usage: 16.1 MB, less than 79.98% of Python3 online submissions for Squares of a Sorted Array.
        """
        nums = [x**2 for x in nums]
        nums.sort()
        return nums

    def twoPointersSortedSquares(self, nums: List[int]) -> List[int]:
        """
        Taking advantage of the fact that the array is in non-decreasing order.

        Example:
            -4 -1 0 3 10
            l  r
                l r       <- find 1st positive element on right side
                l r       <- add square of smallest absolute value, update pointers
                l r       <- [0]
                l   r     <- [0, 1]
            l       r     <- [0, 1, 9]
            l          r  <- [0, 1, 16]
                       r  <- [0, 1, 16, 100]

        Runtime: 441 ms, faster than 16.94% of Python3 online submissions for Squares of a Sorted Array.
        Memory Usage: 16.3 MB, less than 41.60% of Python3 online submissions for Squares of a Sorted Array.
        """
        # 1. find first positive element
        l = 0
        r = 1

        while 0 <= l < r <= len(nums) - 1:
            if nums[r] >= 0:
                break

            l += 1
            r += 1

        # 2. main loop, add smallest absolute value to solution, move pointers
        solution = []

        while 0 <= l < r <= len(nums) - 1:
            if abs(nums[l]) <= abs(nums[r]):
                solution.append(nums[l] ** 2)
                l -= 1
            else:
                solution.append(nums[r] ** 2)
                r += 1

        while 0 <= l:
            solution.append(nums[l] ** 2)
            l -= 1

        while r <= len(nums) - 1:
            solution.append(nums[r] ** 2)
            r += 1

        return solution
