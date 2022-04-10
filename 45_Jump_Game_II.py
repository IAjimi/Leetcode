from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        A bit less clean than 'oldJump' but faster - the first time we
        reach jump[-1] will always be the solution bc jump number is >=
        increasing with ix.

        Runtime: 5424 ms, faster than 25.51% of Python3 online submissions.
        Memory Usage: 15.1 MB, less than 92.57% of Python3 online submissions.
        """
        jump = [10**5 for n in nums]
        jump[0] = 0  # starting point

        ix = 0

        while jump[-1] == 10**5:
            v = nums[ix]
            max_reach = min(ix + v, len(nums) - 1)

            for jx in range(ix, max_reach + 1):
                jump[jx] = min(jump[jx], jump[ix] + 1)

            ix += 1

        return jump[-1]

    def oldJump(self, nums: List[int]) -> int:
        """
        Runtime: 6036 ms, faster than 23.90% of Python3 online submissions for Jump Game II.
        Memory Usage: 15 MB, less than 98.56% of Python3 online submissions for Jump Game II.
        """
        jump = [10**5 for n in nums]
        jump[0] = 0  # starting point

        for ix, v in enumerate(nums):
            max_reach = min(ix + v, len(nums) - 1)
            for jx in range(ix, max_reach + 1):
                jump[jx] = min(jump[jx], jump[ix] + 1)

        return jump[-1]
