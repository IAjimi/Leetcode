from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Runtime: 82 ms, faster than 56.20% of Python3 online submissions for Single Number III.
        Memory Usage: 15.9 MB, less than 62.16% of Python3 online submissions for Single Number III.
        """
        i = 0
        nums = sorted(nums)
        solution = []

        while i <= len(nums) - 2:
            if nums[i] != nums[i + 1]:
                solution.append(nums[i])
                i += 1
            else:
                i += 2

            # return early
            if len(solution) == 2:
                return solution

        # last element is part of solution
        solution.append(nums[i])
        return solution
