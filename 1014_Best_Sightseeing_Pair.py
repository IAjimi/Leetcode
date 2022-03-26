from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Insight: to iterate once over array, only need to keep track of max value.
        Here, max value is a bit trickier because you need to take into account the *index* of the max,
        so the comparison is done by picking the max of values[i] >= values[max_ix] - (i - max_ix)
        when at index i.

        Runtime: 744 ms, faster than 35.20% of Python3 online submissions for Best Sightseeing Pair.
        Memory Usage: 20.7 MB, less than 18.49% of Python3 online submissions for Best Sightseeing Pair.
        """

        max_ix = 0
        score = 0

        for i in range(1, len(values)):
            score = max(score, values[i] + values[max_ix] - (i - max_ix))

            if values[i] >= values[max_ix] - (i - max_ix):
                max_ix = i

        return score
