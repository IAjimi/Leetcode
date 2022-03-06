from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 40 ms, faster than 91.47% of Python3 online submissions for Permutations.
        Memory Usage: 14 MB, less than 91.54% of Python3 online submissions for Permutations.
        """
        if len(nums) == 1:
            return [nums]

        result = []
        permutations = self.permute(nums[1:])

        for p in permutations:
            for i in range(len(p) + 1):
                result.append(p[:i] + [nums[0]] + p[i:])

        return result
