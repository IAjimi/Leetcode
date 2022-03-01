from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Runtime: 83 ms, faster than 60.72% of Python3 online submissions for Single Number II.
        Memory Usage: 15.7 MB, less than 93.27% of Python3 online submissions for Single Number II.
        """

        i = 0
        nums = sorted(nums)

        while i <= len(nums) - 3:
            if nums[i] != nums[i + 1] or nums[i] != nums[i + 2]:
                return nums[i]
            i += 3

        return nums[i]
