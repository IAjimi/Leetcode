from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Runtime: 40 ms, faster than 72.31% of Python3 online submissions for Sort Colors.
        Memory Usage: 13.9 MB, less than 67.55% of Python3 online submissions for Sort Colors.
        """
        counter = {0: 0, 1: 0, 2: 0}

        for n in nums:
            counter[n] += 1

        for i in range(len(nums)):
            if i < counter[0]:
                nums[i] = 0
            elif counter[0] + counter[1] > i >= counter[0]:
                nums[i] = 1
            else:
                nums[i] = 2
