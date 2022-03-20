from collections import Counter


class Solution:
    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            """
            Permutation = substring of FIXED LENGTH with same count of characters as s1.

            Runtime: 108 ms, faster than 62.39% of Python3 online submissions for Permutation in String.
            Memory Usage: 14 MB, less than 52.93% of Python3 online submissions for Permutation in String.
            """
            l = 0
            r = len(s1) - 1

            s1_counter = Counter(s1)
            s2_counter = Counter(s2[:r])

            while 0 <= l <= r <= len(s2) - 1:
                s2_counter[s2[r]] += 1  # while loop enforces r <= len(s2)

                if s1_counter != s2_counter:
                    s2_counter[s2[l]] -= 1
                    l += 1
                    r += 1
                else:
                    return True

            return False
