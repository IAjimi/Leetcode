from typing import List
from heapq import heappush, heapreplace


class KthLargest:
    """
    Runtime: 119 ms, faster than 69.71% of Python3 online submissions for Kth Largest Element in a Stream.
    Memory Usage: 18.2 MB, less than 71.04% of Python3 online submissions for Kth Largest Element in a Stream.
    """

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        # create minHeap
        nums.sort(reverse=True)
        for n in nums[:k]:
            heappush(self.minHeap, n)

    def add(self, val: int) -> int:
        # minHeap too small, add element no matter what
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        # minHeap at max capacity, add only if changes order
        elif val > self.minHeap[0]:
            heapreplace(self.minHeap, val)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
