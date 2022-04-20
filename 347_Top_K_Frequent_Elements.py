from collections import defaultdict
from typing import List

from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 136 ms, faster than 54.65% of Python3 online submissions for Top K Frequent Elements.
        Memory Usage: 18.6 MB, less than 93.88% of Python3 online submissions for Top K Frequent Elements.
        """
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

        freq = list(hashmap.values())
        freq.sort(reverse=True)
        cutoff_value = freq[k - 1]

        return [k for k, v in hashmap.items() if v >= cutoff_value]

    def heapqTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 100 ms, faster than 95.28% of Python3 online submissions for Top K Frequent Elements.
        Memory Usage: 18.6 MB, less than 91.16% of Python3 online submissions for Top K Frequent Elements.
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        maxHeap = []
        for n, count in counter.items():
            heappush(maxHeap, (-count, n))

        res = []
        for _ in range(k):
            count, n = heappop(maxHeap)
            res.append(n)

        return res
