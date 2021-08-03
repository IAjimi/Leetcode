class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""
		Same as 1 - Two Sum.

		Runtime: 64 ms, faster than 64.62% of Python3 online submissions.
		Memory Usage: 15.4 MB, less than 5.28% of Python3 online submissions.
		"""
		hashtable = {}
		for ix in range(len(nums)):
			if nums[ix] in hashtable:
				hashtable[nums[ix]].append(ix + 1)
			else:
				hashtable[nums[ix]] = [ix + 1]

		for ix in range(len(nums)):
			val = nums[ix]
			complement = target - val
			if complement != val and complement in hashtable:
				return [ix + 1, hashtable[complement][0]]
			elif complement == val and len(hashtable[val]) > 1:
				return hashtable[complement][:2]

	def altTwoSum(self, numbers: List[int], target: int) -> List[int]:
		"""
		Brute force. Too slow for Leetcode.
		"""
		for ix in range(len(numbers)):
			val = numbers[ix]
			complement = target - val

			for jx in range(ix + 1, len(numbers)):
				if numbers[jx] == complement:
					return [ix + 1, jx + 1]  # one-indexed