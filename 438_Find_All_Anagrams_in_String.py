from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Runtime: 363 ms, faster than 32.58% of Python3 online submissions for Find All Anagrams in a String.
        Memory Usage: 15.4 MB, less than 6.89% of Python3 online submissions for Find All Anagrams in a String.
        """
        result = []

        if len(p) > len(s):
            return result

        l = 0
        r = len(p) - 1
        anagram_counter = Counter(p)
        window_counter = Counter(s[:r])

        while r <= len(s) - 1:
            window_counter[s[r]] += 1

            if anagram_counter == window_counter:
                result.append(l)

            window_counter[s[l]] -= 1
            l += 1
            r += 1

        return result
