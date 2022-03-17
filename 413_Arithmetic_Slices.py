from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Runtime: 48 ms, faster than 65.59% of Python3 online submissions for Arithmetic Slices.
        Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
        """

        if len(nums) < 3:
            return 0

        l = 0
        r = 2
        count = 0

        while 0 <= l < r <= len(nums) - 1:
            # keep going into 1st valid subsequence of length 3
            if nums[l + 1] - nums[l] != nums[r] - nums[l + 1]:
                l += 1
                r += 1
                continue

            # one valid subsequence
            count += 1

            # try to extend all the way to the right
            while r < len(nums) - 1 and nums[r + 1] - nums[r] == nums[l + 1] - nums[l]:
                count += 1
                r += 1

            # if break, move l by one, reset length of window to 3
            l += 1
            r = l + 2

        return count
