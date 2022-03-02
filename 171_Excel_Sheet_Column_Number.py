class Solution:
    def letterToNumber(self, letter: str) -> int:
        return 1 + ord(letter) - ord("A")

    def titleToNumber(self, columnTitle: str) -> int:
        """
        Runtime: 48 ms, faster than 45.68% of Python3 online submissions for Excel Sheet Column Number.
        Memory Usage: 13.8 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
        """
        n = len(columnTitle)
        colNum = 0

        for i, letter in enumerate(columnTitle):
            colNum += self.letterToNumber(letter) * (26 ** (n - i - 1))

        return colNum
