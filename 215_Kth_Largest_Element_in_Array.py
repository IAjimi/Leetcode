from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Runtime: 63 ms, faster than 95.14% of Python3 online submissions for Kth Largest Element in an Array.
        Memory Usage: 14.7 MB, less than 76.29% of Python3 online submissions for Kth Largest Element in an Array.
        """
        nums.sort()
        return nums[len(nums) - k]
