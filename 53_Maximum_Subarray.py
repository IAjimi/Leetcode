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
        Runtime: 845 ms, faster than 67.89% of Python3 online submissions for Maximum Subarray.
        Memory Usage: 28 MB, less than 57.09% of Python3 online submissions for Maximum Subarray.
        """
        dp = [-(10**5) for _ in nums]

        for i, n in enumerate(nums):
            dp[i] = max(dp[i - 1] + n, n)

        return max(dp)
