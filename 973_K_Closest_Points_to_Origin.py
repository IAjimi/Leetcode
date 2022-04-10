from typing import List
from heapq import heappop, heappush


class Solution:
    def euclidieanDistance(self, point: List[int]) -> int:
        x, y = point
        return (x**2 + y**2) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Runtime: 824 ms, faster than 91.12% of Python3 online submissions for K Closest Points to Origin.
        Memory Usage: 20.5 MB, less than 39.20% of Python3 online submissions for K Closest Points to Origin.
        """
        minHeap = []

        for point in points:
            dist = self.euclidieanDistance(point)
            heappush(minHeap, (dist, point))

        res = [None for _ in range(k)]
        for i in range(k):
            dist, point = heappop(minHeap)
            res[i] = point

        return res
