from typing import List


class Solution:
    def nicerSearch(self, nums: List[int], target: int) -> int:
        """
        Runtime: 444 ms, faster than 13.69% of Python3 online submissions for Binary Search.
        Memory Usage: 15.5 MB, less than 27.89% of Python3 online submissions for Binary Search.
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Runtime: 236 ms, faster than 91.48% of Python3 online submissions for Binary Search.
        Memory Usage: 15.6 MB, less than 19.43% of Python3 online submissions for Binary Search.
        """
        l = 0
        r = len(nums) - 1

        while 0 <= l < r <= len(nums) - 1 and l + 1 < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
