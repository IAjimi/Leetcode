from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 48 ms, faster than 90.30% of Python3 online submissions for Intersection of Two Arrays II.
        Memory Usage: 14.1 MB, less than 54.45% of Python3 online submissions for Intersection of Two Arrays II.
        """
        nums1_counter = Counter(nums1)
        solution = []

        for n in nums2:
            if nums1_counter.get(n, 0) > 0:
                nums1_counter[n] -= 1
                solution.append(n)

        return solution
