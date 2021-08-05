class Solution:
	def maxArea(self, height: List[int]) -> int:
		"""
		Runtime: 748 ms, faster than 57.09% of Python3 online submissions.
		Memory Usage: 27.6 MB, less than 23.75% of Python3 online submissions.
		"""
		max_area = 0
		l, r = 0, len(height) - 1

		while l < r:
			max_area = max(max_area, min(height[l], height[r]) * (r - l))

			if height[l] < height[r]:
				l += 1
			else:
				r += -1

		return max(max_area, min(height[l], height[r]) * (r - l))


if __name__ == '__main__':
	assert 0 == Solution().maxArea([0, 1])
	assert 1 == Solution().maxArea([1, 1])
	assert 1 == Solution().maxArea([1, 2])
	assert 2 == Solution().maxArea([1, 2, 1])
	assert 24 == Solution().maxArea([1, 3, 2, 5, 25, 24, 5])
	assert 49 == Solution().maxArea([1,8,6,2,5,4,8,3,7])
	assert 16 == Solution().maxArea([4, 3, 2, 1, 4])
