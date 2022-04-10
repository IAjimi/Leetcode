from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Top 20% by speed.
        """
        num = int("".join([str(s) for s in digits]))
        num += 1
        num = str(num)
        num = [int(n) for n in num]
        return num
