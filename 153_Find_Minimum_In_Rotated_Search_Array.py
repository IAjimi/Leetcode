from typing import List


class Solution:
    def findMin(self, nums):
        """
        July 30, 2021.

        Runtime: 44 ms, faster than 35.37% of Python3 online submissions.
        Memory Usage: 14.7 MB.
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        else:
            left, right = 0, len(nums) - 1

            while right - left > 1:
                if nums[right] >= nums[left]:
                    right = (right + left) // 2
                else:
                    left = (right + left) // 2

            while nums[left] > nums[left - 1]:
                left += -1

            return nums[left]

    def findMin(self, nums: List[int]) -> int:
        """
        August 31, 2021.

        Runtime: 40 ms, faster than 68.58% of Python3 online submissions.
        Memory Usage: 14.7 MB.
        """
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (r + l) // 2

            if nums[l] < nums[mid] < nums[r]:
                # sorted array, regular binary search
                if nums[l] < nums[mid]:
                    r = mid
                else:
                    l = mid
            elif nums[r] > nums[l] > nums[mid] or nums[l] > nums[r] > nums[mid]:
                # min is between l and m
                r = mid
            elif nums[mid] > nums[l] > nums[r]:
                # min is between mid and r
                l = mid
            else:
                raise Exception

        return min(nums[l], nums[r])
