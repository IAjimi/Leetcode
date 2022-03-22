from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Runtime: 569 ms, faster than 70.61% of Python3 online submissions for Jump Game.
        Memory Usage: 15.2 MB, less than 56.56% of Python3 online submissions for Jump Game.
        """
        start = 0
        end = nums[0]

        while start < end < len(nums):
            max_ix = start

            for j in range(start + 1, end + 1):
                if j >= len(nums) - 1:
                    return True

                max_ix = max(max_ix, j + nums[j])

            start = end
            end = max_ix

        return end >= len(nums) - 1
