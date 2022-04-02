from typing import List


class Solution:
    def isArithmeticSubarray(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()
        diff = nums[1] - nums[0]

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != diff:
                return False

        return True

    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        """
        Runtime: 317 ms, faster than 37.85% of Python3 online submissions for Arithmetic Subarrays.
        Memory Usage: 14.1 MB, less than 96.19% of Python3 online submissions for Arithmetic Subarrays.
        """
        solution = []

        for left, right in zip(l, r):
            res = self.isArithmeticSubarray(nums[left : right + 1])
            solution.append(res)

        return solution
