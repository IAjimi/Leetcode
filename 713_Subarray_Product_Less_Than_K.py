from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Runtime: 1341 ms, faster than 10.99% of Python3 online submissions for Subarray Product Less Than K.
        Memory Usage: 16.7 MB, less than 38.39% of Python3 online submissions for Subarray Product Less Than K.
        """
        l = 0
        r = 0
        cur_prod = nums[l]
        count = 0

        while l <= r < len(nums):
            if cur_prod < k:
                count += 1 + r - l
                r += 1
                if r <= len(nums) - 1:
                    cur_prod *= nums[r]
            else:
                cur_prod = cur_prod / nums[l]
                l += 1
                if len(nums) > l > r:
                    r = l
                    cur_prod = nums[l]

        return count
