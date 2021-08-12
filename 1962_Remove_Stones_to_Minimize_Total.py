import heapq
import math


class Solution:
	def minStoneSum(self, piles, k):
		"""
		Runtime: 2084 ms, faster than 54.99% of Python3 online submissions.
		Memory Usage: 28.9 MB, less than 45.80% of Python3 online submissions.

		Idea: using max-heap to find the max of the array repeatedly quickly.
		Then, K-times, remove top, halve top, put top back in heap.
		Getting sum by keeping track of the value removed from the max.

		Heapq is a min-heap, so multiplying everything by -1 to get max-heap.
		"""
		total = sum(piles)
		max_heap = [-1 * p for p in piles]
		heapq.heapify(max_heap)

		for i in range(k):
			current_val = -1 * heapq.heappop(max_heap)
			new_val = current_val - math.floor(current_val / 2)
			total -= math.floor(current_val / 2)
			heapq.heappush(max_heap, -1 * new_val)

		return total

if __name__ == '__main__':
	assert 5 == Solution().minStoneSum(piles=[10],k=1)
	assert 15 == Solution().minStoneSum(piles=[10,10], k=1)