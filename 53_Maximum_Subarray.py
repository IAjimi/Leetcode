from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Runtime: 68 ms, faster than 55.03% of Python3 online submissions.
        Memory Usage: 14.9 MB, less than 95.7% of Python3 online submissions.
        """
        # case with array filled with negative numbers
        if max(nums) < 0:
            return max(nums)

        max_sum = 0
        current_sum = 0

        for val in nums:
            # if adding val still results in positive value, keep
            if val + current_sum > 0:
                current_sum += val
            # otherwise reset
            else:
                current_sum = 0

            max_sum = max(max_sum, current_sum)

        return max_sum

    def otherDPMaxSubArray(self, nums: List[int]) -> int:
        """
        Note: could store only previous result instead of dp array.

        Runtime: 1101 ms, faster than 37.13% of Python3 online submissions for Maximum Subarray.
        Memory Usage: 28 MB, less than 76.61% of Python3 online submissions for Maximum Subarray.
        """
        dp = [None for n in nums]

        for i, n in enumerate(nums):
            if i == 0:
                dp[i] = n
            else:
                dp[i] = max(dp[i - 1] + n, n)

        return max(dp)
