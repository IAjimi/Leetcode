from typing import List


class Solution:
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 8321 ms, faster than 5.00% of Python3 online submissions for 3Sum.
        Memory Usage: 17.9 MB, less than 83.09% of Python3 online submissions for 3Sum.
        """
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])
                k = self.binary_search(nums, j + 1, len(nums) - 1, target)
                if k != -1:
                    triplet = [nums[i], nums[j], target]
                    res.append(triplet)

        return res
