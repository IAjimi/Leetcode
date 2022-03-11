from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Runtime: 39 ms, faster than 92.75% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
        Memory Usage: 14.1 MB, less than 78.41% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
        """
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while 0 <= left <= right <= len(nums) - 1:
            mid = (left + right) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid == 0 and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    assert 0 == Solution().findMin([0])
    assert 1 == Solution().findMin([1, 2])
    assert 1 == Solution().findMin([2, 1])
    assert 1 == Solution().findMin([3, 1, 2])
    assert 1 == Solution().findMin([2, 3, 1])
    assert 1 == Solution().findMin([3, 4, 5, 1, 2])
    assert 0 == Solution().findMin([4, 5, 6, 7, 0, 1, 2])
    assert 11 == Solution().findMin([11, 13, 15, 17])
