from typing import List


class Solution:
    def getIntersection(self, s1: int, e1: int, s2: int, e2: int) -> List[int]:
        """Return intersection interval given 2 intersecting arrays"""
        int_start = max(s1, s2)
        int_end = min(e1, e2)
        return [int_start, int_end]

    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        """
        Runtime: 172 ms, faster than 71.80% of Python3 online submissions for Interval List Intersections.
        Memory Usage: 14.8 MB, less than 65.49% of Python3 online submissions for Interval List Intersections.
        """
        output = []
        int1 = 0
        int2 = 0

        while int1 < len(firstList) and int2 < len(secondList):
            s1, e1 = firstList[int1]
            s2, e2 = secondList[int2]

            # no intersection
            if s1 > e2:
                int2 += 1
                continue
            elif s2 > e1:
                int1 += 1
                continue

            # one interval is subset of another
            if s1 <= s2 <= e2 <= e1:
                int2 += 1
            elif s2 <= s1 <= e1 <= e2:
                int1 += 1
            # interval overlap
            elif s2 <= e1 <= e2:
                int1 += 1
            elif s1 <= e2 <= e1:
                int2 += 1

            output.append(self.getIntersection(s1, e1, s2, e2))

        return output
