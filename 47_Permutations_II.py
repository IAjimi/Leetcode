from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 144 ms, faster than 27.61% of Python3 online submissions for Permutations II.
        Memory Usage: 14.2 MB, less than 82.91% of Python3 online submissions for Permutations II.
        """
        if len(nums) == 1:
            return [nums]

        result = []
        permutations = self.permuteUnique(nums[1:])

        for p in permutations:
            for i in range(len(p) + 1):
                new_p = p[:i] + [nums[0]] + p[i:]
                if new_p not in result:
                    result.append(new_p)

        return result
