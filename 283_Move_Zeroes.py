from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Runtime: 184 ms, faster than 74.42% of Python3 online submissions for Move Zeroes.
        Memory Usage: 15.7 MB, less than 15.19% of Python3 online submissions for Move Zeroes.
        """
        l = 0
        r = 1

        while 0 <= l < r <= len(nums) - 1:
            # move left pointer to reach 0
            if nums[l] != 0:
                l += 1
                r += 1
            # move right to reach non zero element
            elif nums[r] == 0:
                r += 1
            # left is 0, right is non zero -> swap
            else:
                nums[l], nums[r] = nums[r], nums[l]
