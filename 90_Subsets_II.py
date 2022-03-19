from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 81 ms, faster than 9.68% of Python3 online submissions for Subsets II.
        Memory Usage: 14.2 MB, less than 26.59% of Python3 online submissions for Subsets II.
        """
        if not nums:
            return [[]]

        prev = self.subsetsWithDup(nums[1:])
        result = prev.copy()

        for subset in prev:
            new_subset = subset + [nums[0]]
            new_subset.sort()
            if new_subset not in result:
                result.append(new_subset)

        return result
