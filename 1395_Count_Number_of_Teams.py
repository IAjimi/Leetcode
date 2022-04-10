from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        Runtime: 876 ms, faster than 88.86% of Python3 online submissions.
        Memory Usage: 14.5 MB, less than 46.31% of Python3 online submissions.
        """
        counter = 0

        # Only iterate over elements in the middle (the js in the problem description)
        for j in range(1, len(rating) - 1):
            left_small, right_small = 0, 0

            # look to the left
            for i in range(j):
                if rating[i] < rating[j]:
                    left_small += 1

            # look to the right
            for k in range(j + 1, len(rating)):
                if rating[k] < rating[j]:
                    right_small += 1

            # since elements are unique, can use left_small and right_small to deduce
            # number of elements bigger than j in the left and right handside
            left_big = max(j - left_small, 0)
            right_big = max((len(rating) - j - 1) - right_small, 0)

            counter += (left_small * right_big) + (left_big * right_small)

        return counter
