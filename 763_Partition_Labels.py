from typing import List, Dict


class Solution:
    def collectIntervals(self, s: str) -> Dict[str, List[int]]:
        intervals = {}

        for i, v in enumerate(s):
            if v not in intervals:
                intervals[v] = [i, i]
            else:
                intervals[v][1] = i

        return intervals

    def partitionLabels(self, s: str) -> List[int]:
        """
        Trick is to realize we are looking for the length of all overlapping intervals.

        Runtime: 63 ms, faster than 42.41% of Python3 online submissions for Partition Labels.
        Memory Usage: 13.9 MB, less than 36.30% of Python3 online submissions for Partition Labels.
        """
        # 1st. we collect intervals for every letter (one pass, O(n))
        intervals = self.collectIntervals(s)
        intervals = sorted(list(intervals.values()), key=lambda i: i[0])

        # 2. we merge intervals
        result = []
        l = 0
        r = 1

        while l < r < len(intervals):
            s1, e1 = intervals[l]
            s2, e2 = intervals[r]

            # r is contained by l
            if s1 <= s2 <= e2 <= e1:
                r += 1
            # r intersects with l
            elif s1 <= s2 <= e1 <= e2:
                intervals[l][1] = intervals[r][1]
                r += 1
            # no intersection, move l to the right
            elif e1 < e2:
                result.append(1 + e1 - s1)
                l = r
                r += 1

        result.append(1 + intervals[l][1] - intervals[l][0])
        return result
