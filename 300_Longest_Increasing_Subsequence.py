from typing import List
from heapq import heappop, heappush


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Runtime: 7161 ms, faster than 5.89% of Python3 online submissions for Longest Increasing Subsequence.
        Memory Usage: 14.7 MB, less than 12.01% of Python3 online submissions for Longest Increasing Subsequence.
        """
        h = [(0, -(10**5))]

        for n in nums:
            popped_solutions = []

            while h:
                # pop until find suitable solution
                count, max_val = heappop(h)

                popped_solutions.append((count, max_val))

                if max_val < n:
                    count -= 1
                    popped_solutions.append((count, n))

                    # push everything back in
                    for count, max_val in popped_solutions:
                        heappush(h, (count, max_val))

                    break

        solution, _ = heappop(h)
        return -solution
