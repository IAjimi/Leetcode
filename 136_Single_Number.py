from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Runtime: 213 ms, faster than 40.93% of Python3 online submissions for Single Number.
        Memory Usage: 16.9 MB, less than 10.15% of Python3 online submissions for Single Number.
        """
        i = 0
        nums = sorted(nums)

        while i <= len(nums) - 2:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2

        return nums[i]
