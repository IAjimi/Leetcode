from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Runtime: 593 ms, faster than 20.14% of Python3 online submissions for Max Consecutive Ones.
        Memory Usage: 14.4 MB, less than 38.10% of Python3 online submissions for Max Consecutive Ones.
        """
        if sum(nums) == 0:
            return 0

        l = 0
        r = 1
        max_length = 0

        while l < r <= len(nums) - 1:
            if nums[l] == 0:
                l += 1
                r += 1
                continue  # make sure conditions get checked

            if nums[r] == 0:
                max_length = max(max_length, r - l)
                l = r + 1
                r = l + 1
            else:
                r += 1

        max_length = max(max_length, r - l)
        return max_length
