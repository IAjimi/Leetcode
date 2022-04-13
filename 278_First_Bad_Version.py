# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 80.57% of Python3 online submissions for First Bad Version.
        Memory Usage: 13.8 MB, less than 86.07% of Python3 online submissions for First Bad Version.
        """
        l = 0
        r = n

        while 0 <= l < r <= n and l + 1 < r:
            m = (l + r) // 2

            if isBadVersion(m):
                r = m
            else:
                l = m

        if isBadVersion(l):
            return l
        else:
            return r
