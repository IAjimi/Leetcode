from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        """
        Runtime: 680 ms, faster than 71.87% of Python3 online submissions for Maximize the Topmost Element After K Moves.
        Memory Usage: 27.9 MB, less than 54.94% of Python3 online submissions for Maximize the Topmost Element After K Moves.
        """
        # empty pile
        if len(nums) == 1 and k % 2 != 0:
            return -1

        # find max in array given conditions
        max_val = 0
        for i, n in enumerate(nums):
            # index i is available if k >= i AND k != i + 1
            if (k >= i) & (k != i + 1):
                max_val = max(max_val, n)
            elif i > k:
                break

        return max_val
