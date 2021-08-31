class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        """
        Maximize product difference by maximizing one product and minimizing the other.

        Runtime: 296 ms, faster than 5.27% of Python3 online submissions.
		Memory Usage: 15.5 MB, less than 46.08% of Python3 online submissions.
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]