class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Runtime: 89 ms, faster than 22.06% of Python3 online submissions for Valid Anagram.
        Memory Usage: 15.2 MB, less than 6.90% of Python3 online submissions for Valid Anagram.
        """
        s = sorted(s)  # O(log n)
        t = sorted(t)  # O(log n)
        return s == t
