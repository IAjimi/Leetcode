from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> str:
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)

    def reverseWords(self, s: str) -> str:
        """
        Runtime: 244 ms, faster than 5.11% of Python3 online submissions for Reverse Words in a String III.
        Memory Usage: 14.8 MB, less than 35.42% of Python3 online submissions for Reverse Words in a String III.
        """
        s = [char for char in s]
        l = 0
        r = 1
        sol = ""

        while 0 <= l < r <= len(s):
            # find end of word
            while r < len(s) - 1 and s[r] != " ":
                r += 1

            if r == len(s) - 1:
                r += 1

            # reverse word
            sol += self.reverseString(s[l:r])
            sol += " " if r < len(s) - 1 else ""

            # update pointers
            l = r + 1
            r = l + 1

        return sol
