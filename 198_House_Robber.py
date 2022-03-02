from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Two states:
            * Cooldown: don't do anything, get max of previous round
            * Rob: rob house - can't access rob[i-1] loot

        Runtime: 24 ms, faster than 98.74% of Python3 online submissions for House Robber.
        Memory Usage: 14 MB, less than 65.80% of Python3 online submissions for House Robber.
        """

        if len(nums) == 1:
            return nums[0]

        cooldown = [0 for _ in nums]
        rob = [0 for _ in nums]

        for i in range(len(nums)):
            cooldown[i] = max(cooldown[i - 1], rob[i - 1])
            rob[i] = max(cooldown[i - 1], rob[i - 2]) + nums[i]

        return max(cooldown[-1], rob[-1])
