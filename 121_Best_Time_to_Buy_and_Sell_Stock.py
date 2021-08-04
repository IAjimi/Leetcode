class Solution:
	def maxProfit(self, prices):
		"""
		Greedy method.

		Runtime: 976 ms, faster than 78.23% of Python3 online submissions.
		Memory Usage: 25.1 MB, less than 82.67% of Python3 online submissions.
		"""
		if len(prices) == 1:
			return 0
		else:
			local_min, local_max = prices[0], prices[1]
			max_gain = max(local_max - local_min, 0)

			for ix in range(1, len(prices)):
				if prices[ix] < local_min and ix <= len(prices) - 2:
					local_min = prices[ix]
					local_max = prices[ix + 1]
					max_gain = max(local_max - local_min, max_gain)
				if prices[ix] > local_max:
					local_max = prices[ix]
					max_gain = max(local_max - local_min, max_gain)

			return max_gain


	def altMaxProfit(self, prices):
		"""
		Too slow.
		"""
		ix = sorted(range(len(prices)), key=prices.__getitem__)
		prices.sort()

		best_gain = 0
		l, r = 0, max(ix)

		while r > l:
			# Find highest possible sale price
			while ix[r] < ix[l] and r > l:
				r += -1

			# Update sale price
			best_gain = max(prices[r] - prices[l], best_gain)

			l += 1
			r = max(ix)

		return best_gain

def test_maxProfit():
	assert 0 == Solution().maxProfit([0])
	assert 1 == Solution().maxProfit([0, 1])
	assert 0 == Solution().maxProfit([1, 0])
	assert 2 == Solution().maxProfit([0, 1, 2])
	assert 2 == Solution().maxProfit([1, 0, 2])
	assert 2 == Solution().maxProfit([2, 4, 1])
	assert 3 == Solution().maxProfit([4, 7, 1, 2])
	assert 5 == Solution().maxProfit([7, 1, 5, 3, 6, 4])
	assert 0 == Solution().maxProfit([7, 6, 4, 3, 1])

