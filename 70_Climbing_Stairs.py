class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Runtime: 24 ms, faster than 95.04% of Python3 online submissions.
        Memory Usage: 14.3 MB, less than 11.50% of Python3 online submissions.
        """
        if n <= 2:
            return n
        else:
            twice_before = 1
            once_before = 2

            for ix in range(2, n):
                steps = once_before + twice_before
                once_before, twice_before = steps, once_before

            return steps
