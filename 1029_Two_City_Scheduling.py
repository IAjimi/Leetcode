from typing import List, Set, Tuple
from heapq import heappop, heappush


class Solution:
    def initialAlloc(self, costs: List[List[int]]) -> Tuple[Set[int], Set[int]]:
        a = set()
        b = set()

        for i, n in enumerate(costs):
            if n[0] < n[1]:
                a.add(i)
            else:
                b.add(i)

        return a, b

    def createHeap(
        self, costs: List[List[int]], cur_set: Set[int]
    ) -> List[Tuple[int, int]]:
        q = []
        for i, n in enumerate(costs):
            if i in set(cur_set):
                heappush(q, (abs(n[0] - n[1]), i))

        return q

    def updateSet(
        self,
        imbalance: int,
        q: List[Tuple[int, int]],
        old_set: Set[int],
        new_set: Set[int],
    ) -> Tuple[Set[int], Set[int]]:
        reallocate_num = abs(imbalance // 2)
        for _ in range(reallocate_num):
            cost, person = heappop(q)
            old_set.remove(person)
            new_set.add(person)

        return old_set, new_set

    def computeCost(self, costs: List[List[int]], a: Set[int]) -> int:
        """Return the total cost of the trips given the memberships in set a."""
        total = 0
        for i, n in enumerate(costs):
            if i in a:
                total += n[0]
            else:
                total += n[1]
        return total

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Runtime: 81 ms, faster than 16.03% of Python3 online submissions for Two City Scheduling.
        Memory Usage: 13.7 MB, less than 98.73% of Python3 online submissions for Two City Scheduling.
        """
        # allocate based on min price
        a, b = self.initialAlloc(costs)

        # change allocation to have even sets
        imbalance = len(a) - len(b)

        # more people in a than b
        if imbalance > 0:
            # add all prices to heap
            q = self.createHeap(costs, a)

            # push and add to set
            a, b = self.updateSet(imbalance, q, a, b)
        else:
            q = self.createHeap(costs, b)
            b, a = self.updateSet(-imbalance, q, b, a)

        total = self.computeCost(costs, a)

        return total
