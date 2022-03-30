from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        O(n) time, O(m) space where m is the number of unique values in nums.

        Runtime: 724 ms, faster than 71.93% of Python3 online submissions for Max Number of K-Sum Pairs.
        Memory Usage: 27.4 MB, less than 27.64% of Python3 online submissions for Max Number of K-Sum Pairs.
        """
        sol = 0
        hashmap = defaultdict(int)

        for n in nums:
            target = k - n
            if hashmap[target] > 0:
                hashmap[target] -= 1
                sol += 1
            else:
                hashmap[n] += 1

        return sol
