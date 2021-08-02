class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		"""
		Runtime: 60 ms, faster than 89.50% of Python3 online submissions.
		Memory Usage: 15.1 MB, less than 45.75% of Python3 online submissions.
		"""
		nums.sort(reverse=True)
		return nums[k - 1]
