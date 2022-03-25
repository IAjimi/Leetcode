from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Runtime: 616 ms, faster than 48.52% of Python3 online submissions for Boats to Save People.
        Memory Usage: 21 MB, less than 34.38% of Python3 online submissions for Boats to Save People.
        """
        people.sort()

        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            if people[r] >= limit:
                count += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                count += 1
                r -= 1

        return count
