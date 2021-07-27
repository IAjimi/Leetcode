class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		"""
		Runtime: 48 ms, faster than 50.60% of Python3 online submissions.
		Memory Usage: 14.5 MB, less than 11.34% of Python3 online submissions.

		Meant to be done with binary search for log(n)
		https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
		"""
		if len(nums) == 1:
			return 0

		for ix in range(len(nums)):
			if ix == 0 and nums[ix] > nums[ix + 1]:
				return 0
			elif ix < len(nums) - 1 and nums[ix] > nums[ix + 1] and nums[ix] > nums[ix - 1]:
				return ix
			elif ix == len(nums) - 1 and nums[ix] > nums[ix - 1]:
				return len(nums) - 1
