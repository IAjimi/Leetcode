from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        O(n) time, O(1) space.

        Runtime: 227 ms, faster than 50.36% of Python3 online submissions for Majority Element.
        Memory Usage: 15.5 MB, less than 81.81% of Python3 online submissions for Majority Element.
        """
        nums.sort()
        counter = 0
        cur_val = None

        for val in nums:
            if val != cur_val:
                counter = 0  # reset counter
                cur_val = val

            counter += 1

            if counter >= 1 + (len(nums) // 2):
                return val

    def AltMajorityElement(self, nums: List[int]) -> int:
        """
        Faster implementation (still O(n)) but uses more memory (O(m) where m is the number
        of distinct values in nums).

        Runtime: 180 ms, faster than 31.31% of Python3 online submissions for Majority Element.
        Memory Usage: 15.6 MB, less than 12.08% of Python3 online submissions for Majority Element.
        """
        nums.sort()
        counter = defaultdict(int)

        for val in nums:
            counter[val] += 1
            if counter[val] >= 1 + (len(nums) // 2):
                return val

        return -1
