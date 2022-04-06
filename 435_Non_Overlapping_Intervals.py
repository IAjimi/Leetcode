from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Runtime: 1288 ms, faster than 99.76% of Python3 online submissions for Non-overlapping Intervals.
        Memory Usage: 53 MB, less than 23.89% of Python3 online submissions for Non-overlapping Intervals.
        """
        intervals = sorted(intervals, key=lambda i: i[1])  # sort by earliest end time

        count = 0
        prev_start, prev_end = -(10**8), -(10**8)

        for start, end in intervals:
            # no intersection
            if start >= prev_end:
                prev_start, prev_end = start, end
            # intersection
            else:
                count += 1

        return count
