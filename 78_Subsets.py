from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 67 ms, faster than 12.41% of Python3 online submissions for Subsets.
        Memory Usage: 14 MB, less than 83.03% of Python3 online submissions for Subsets.
        """
        if not nums:
            return [[]]

        prev = self.subsets(nums[1:])
        cur = []

        for subset in prev:
            cur.append(subset + [nums[0]])

        return prev + cur
