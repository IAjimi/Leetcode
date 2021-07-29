class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		"""
		Attempt to run in O(n) with O(1) memory.

		Runtime: 188 ms, faster than 24.24% of Python3 online submissions.
		Memory Usage: 15.5 MB, less than 82.30% of Python3 online submissions.
		"""
		nums.sort()
		cur_count, max_count = 0, 0
		max_val = nums[0]

		for ix in range(1, len(nums)):
			if nums[ix] != nums[ix - 1] or ix == len(nums) - 1:
				max_val = nums[ix - 1] if cur_count > max_count else max_val
				max_count = max(max_count, cur_count)
				cur_count = 1
			else:
				cur_count += 1

			if max_count >= 1 + (len(nums) / 2):
				return max_val

		return max_val

	def AltMajorityElement(self, nums: List[int]) -> int:
		"""
		Faster but uses more memory.

		Runtime: 180 ms, faster than 31.31% of Python3 online submissions for Majority Element.
		Memory Usage: 15.6 MB, less than 12.08% of Python3 online submissions for Majority Element.
		"""
		nums.sort()
		counter = defaultdict(int)

		for val in nums:
			counter[val] += 1
			if counter[val] >= 1 + (len(nums) // 2):
				return val

		return -1
