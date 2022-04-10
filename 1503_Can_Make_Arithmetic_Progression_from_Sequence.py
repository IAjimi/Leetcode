from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Runtime: 48 ms, faster than 19.70% of Python3 online submissions.
        Memory Usage: 14.3 MB, less than 63.24% of Python3 online submissions
        """
        arr.sort()
        prev_diff = None

        for ix in range(len(arr) - 1):
            difference = abs(arr[ix] - arr[ix + 1])

            if prev_diff and prev_diff != difference:
                return False

            prev_diff = difference

        return True
