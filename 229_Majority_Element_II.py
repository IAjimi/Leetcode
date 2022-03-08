import math
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Runtime: 120 ms, faster than 80.80% of Python3 online submissions for Majority Element II.
        Memory Usage: 15.3 MB, less than 54.38% of Python3 online submissions for Majority Element II.
        """
        solution = set()
        hashmap = defaultdict(int)
        target = math.floor(len(nums) / 3)

        for val in nums:
            hashmap[val] += 1

            if hashmap[val] > target:
                solution.add(val)

        return list(solution)

    def sortedMajorityElement(self, nums: List[int]) -> List[int]:
        """
        Runtime: 151 ms, faster than 53.46% of Python3 online submissions for Majority Element II.
        Memory Usage: 15.4 MB, less than 54.38% of Python3 online submissions for Majority Element II.
        """
        solution = set()
        target = math.floor(len(nums) / 3)

        nums.sort()

        counter = 0
        cur_val = None

        for val in nums:
            if val != cur_val:
                counter = 0
                cur_val = val

            counter += 1

            if counter > target:
                solution.add(val)

        return list(solution)
