from typing import List
from heapq import heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Speed: O(n log n) since heappop, heappush are log n

        Runtime: 34 ms, faster than 82.01% of Python3 online submissions for Last Stone Weight.
        Memory Usage: 13.9 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.
        """
        # create max heap
        maxHeap = []
        for n in stones:
            heappush(maxHeap, -n)

        # run algo
        while len(maxHeap) >= 2:
            biggestStone = -heappop(maxHeap)
            bigStone = -heappop(maxHeap)

            if biggestStone > bigStone:
                heappush(maxHeap, bigStone - biggestStone)

        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0
