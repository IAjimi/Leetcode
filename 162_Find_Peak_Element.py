from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Key element is is that all values in nums are different from their neighbor.

        Runtime: 58 ms, faster than 64.17% of Python3 online submissions for Find Peak Element.
                Memory Usage: 14 MB, less than 91.06% of Python3 online submissions for Find Peak Element.
        """
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while 0 <= left <= right <= len(nums) - 1:
            mid = (left + right) // 2

            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
