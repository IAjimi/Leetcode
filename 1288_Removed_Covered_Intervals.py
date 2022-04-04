from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Brute force solution.

        Runtime: 960 ms, faster than 5.20% of Python3 online submissions for Remove Covered Intervals.
        Memory Usage: 14.5 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
        """
        if len(intervals) == 1:
            return 1

        removed = set()

        for i, int_i in enumerate(intervals):
            for int_j in intervals[i + 1 :]:
                if tuple(int_j) in removed or tuple(int_i) in removed:
                    continue

                if int_j[0] <= int_i[0] and int_i[1] <= int_j[1]:
                    removed.add(tuple(int_i))
                elif int_i[0] <= int_j[0] and int_j[1] <= int_i[1]:
                    removed.add(tuple(int_j))

        return len(intervals) - len(removed)


if __name__ == "__main__":
    assert Solution().removeCoveredIntervals([1, 4]) == 1
    assert Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    assert Solution().removeCoveredIntervals([[1, 3], [3, 6], [2, 8], [0, 10]]) == 1
    assert Solution([[1, 4], [2, 3]]) == 1
