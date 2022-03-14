from typing import List


class Solution:
    def binarySearch(self, nums: List[int], left: int, target: int):
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 319 ms, faster than 5.22% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
        Memory Usage: 14.9 MB, less than 27.04% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
        """
        for i, n in enumerate(nums):
            ix = self.binarySearch(nums, i + 1, target - n)
            if ix != -1:
                return [i + 1, ix + 1]

        return [-1, -1]
