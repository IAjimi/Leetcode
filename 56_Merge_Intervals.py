class Solution:
    def merge(self, intervals):
        """
        Runtime: 96 ms, faster than 18.32% of Python3 online submissions for Merge Intervals.
        Memory Usage: 16 MB, less than 83.80% of Python3 online submissions for Merge Intervals.
        """
        intervals = sorted(intervals, key=lambda i: i[0])
        l, r = 0, 1

        while r <= len(intervals) - 1:
            if intervals[l][0] <= intervals[r][0] <= intervals[l][1]:
                intervals[l][0] = min(intervals[l][0], intervals[r][0])
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                del intervals[r]
            else:
                l += 1
                r += 1

        return intervals


if __name__ == "__main__":
    assert [[1, 3], [5, 6], [8, 18]] == Solution().merge(
        intervals=[[1, 3], [5, 6], [8, 10], [9, 18]]
    )
    assert [[1, 6], [8, 10], [15, 18]] == Solution().merge(
        intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]
    )
    assert [[1, 5]] == Solution().merge(intervals=[[1, 4], [4, 5]])
    assert [[1, 5]] == Solution().merge(intervals=[[1, 5]])
    assert [[0, 4]] == Solution().merge(intervals=[[1, 4], [0, 4]])
    assert [[0, 4]] == Solution().merge(intervals=[[1, 4], [0, 1]])
    assert [[1, 10]] == Solution().merge(
        intervals=[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    )
    assert [[0, 5]] == Solution().merge(intervals=[[1, 4], [0, 2], [3, 5]])
    assert [[2, 4], [5, 5]] == Solution().merge(
        intervals=[[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
    )
