from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Runtime: 81 ms, faster than 52.27% of Python3 online submissions for Min Cost Climbing Stairs.
        Memory Usage: 14.1 MB, less than 79.58% of Python3 online submissions for Min Cost Climbing Stairs.
        """
        one_before = cost[1]
        two_before = cost[0]

        for i in range(2, len(cost)):
            current = min(one_before, two_before) + cost[i]
            two_before, one_before = one_before, current

        return min(one_before, two_before)
