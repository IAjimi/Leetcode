from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Runtime: 95 ms, faster than 11.21% of Python3 online submissions for Slowest Key.
        Memory Usage: 14.5 MB, less than 56.54% of Python3 online submissions for Slowest Key.
        """
        max_val = releaseTimes[0]
        max_key = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            cur_key = keysPressed[i]

            if duration > max_val:
                max_val = duration
                max_key = cur_key
            elif duration == max_val and cur_key > max_key:
                max_val = duration
                max_key = cur_key

        return max_key
