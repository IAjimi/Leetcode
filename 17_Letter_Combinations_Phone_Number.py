from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Runtime: 58 ms, faster than 15.94% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 13.9 MB, less than 81.78% of Python3 online submissions for Letter Combinations of a Phone Number.
        """
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if digits == "":
            return []

        prev = self.letterCombinations(digits[1:])
        prev = prev if prev else [""]
        cur_digit = letter_map[digits[0]]

        res = []
        for d in cur_digit:
            new = [d + p for p in prev]
            res.extend(new)

        return res
