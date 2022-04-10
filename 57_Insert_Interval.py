class Solution:
    def insert(self, intervals, newInterval):
        """
        Slightly convoluted code. Iterate over array: determine if must be merged or not.

        Runtime: 84 ms, faster than 38.30% of Python3 online submissions.
        Memory Usage: 17.6 MB, less than 33.43% of Python3 online submissions.
        """
        if not intervals:
            return [newInterval]
        else:
            new_start, new_end = newInterval
            solution = []
            prev_e1 = -1  # trick for insert newInterval at start of array
            merged = False
            added = False

            for ix in range(len(intervals)):
                s1, e1 = intervals[ix]

                # Case 1: interval is subset of new interval
                if new_start <= s1 <= e1 <= new_end:
                    merged = True
                # Case 2: start of new interval is in interval
                elif s1 <= new_start <= e1:
                    merged = True
                # Case 3: end of new interval is in interval
                elif s1 <= new_end <= e1:
                    merged = True
                # Case 4: unmerged new interval is in between 2 intervals
                elif not merged and prev_e1 < new_end < s1:
                    solution.append(newInterval)
                    solution.append(intervals[ix])
                    added = True  # flag here otherwise interval will also be added at end of array
                else:
                    solution.append(intervals[ix])
                    merged = False

                # Add dummy interval in the right spot
                if merged and not added:
                    solution.append(intervals[ix])
                    added = True

                # If still in merge state, adapt merged interval to new interval being merged
                if merged:
                    solution[-1][0] = min(solution[-1][0], new_start, s1)
                    solution[-1][1] = max(solution[-1][1], new_end, e1)

                prev_e1 = e1

            if not added:
                solution.append(newInterval)

            return solution


if __name__ == "__main__":
    assert [[0, 0], [1, 3], [6, 9]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[0, 0]
    )  # first interval
    assert [[1, 5], [6, 9]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[2, 5]
    )  # merge into interval
    assert [[1, 3], [5, 13]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[5, 13]
    )  # merge into interval
    assert [[0, 13]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[0, 13]
    )  # merge all intervals
    assert [[1, 3], [4, 5], [6, 9]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[4, 5]
    )  # in between intervals
    assert [[1, 3], [6, 9], [11, 13]] == Solution().insert(
        intervals=[[1, 3], [6, 9]], newInterval=[11, 13]
    )  # last interval

    assert [[0, 0], [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] == Solution().insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[0, 0]
    )
    assert [[1, 2], [3, 5], [6, 7], [8, 10], [11, 11], [12, 16]] == Solution().insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[11, 11]
    )
    assert [[0, 11], [12, 16]] == Solution().insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[0, 11]
    )
