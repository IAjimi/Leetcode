from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Runtime: 90 ms, faster than 44.12% of Python3 online submissions for Letter Case Permutation.
        Memory Usage: 14.7 MB, less than 86.92% of Python3 online submissions for Letter Case Permutation.

        Recursion: add upper / lower case version of 1st character in string to transformed rest of the
        string.

        Example:
            > a1b2  ["a1b2", "A1b2", "a1B2", "A1B2"]
            # .1b2  ["1b2", "1B2"]
            # ..b2  ["b2", "B2"]
            # ...2  ["2"]
            # ....  [""]
        """
        if s == "":
            return [s]

        permutations = self.letterCasePermutation(s[1:])
        permutations_w_lowercase = [s[0] + p for p in permutations]

        if s[0].isalpha():
            permutations_w_uppercase = [s[0].swapcase() + p for p in permutations]
        else:
            permutations_w_uppercase = []

        return permutations_w_lowercase + permutations_w_uppercase

    def iterLetterCasePermutation(self, s: str) -> List[str]:
        """
        Runtime: 90 ms, faster than 44.12% of Python3 online submissions for Letter Case Permutation.
        Memory Usage: 14.8 MB, less than 66.94% of Python3 online submissions for Letter Case Permutation.
        """
        result = [""]

        for char in s:
            if char.isalpha():
                result = [r + char for r in result] + [
                    r + char.swapcase() for r in result
                ]
            else:
                result = [r + char for r in result]

        return result
