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

