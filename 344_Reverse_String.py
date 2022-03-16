from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Runtime: 361 ms, faster than 18.63% of Python3 online submissions for Reverse String.
        Memory Usage: 18.6 MB, less than 45.15% of Python3 online submissions for Reverse String.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
