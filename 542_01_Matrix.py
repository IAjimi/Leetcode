import heapq
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 752 ms, faster than 51.28% of Python3 online submissions.
        Memory Usage: 17.4 MB, less than 42.63% of Python3 online submissions.

        BFS.
        * list of zeroes (position)
        * move outwards from every zero, keep next nodes in min heap
        * populate old matrix with updated distances
        * terminate when all nodes have been "visited"
        """
        # Fill queue
        targets = set()
        queue = []
        for ix in range(len(matrix)):
            for jx in range(len(matrix[0])):
                if matrix[ix][jx] == 0:
                    heapq.heappush(queue, (0, (ix, jx)))
                else:
                    targets.add((ix, jx))

        while targets:
            steps, new_node = heapq.heappop(queue)

            neighbors = [
                (new_node[0] - 1, new_node[1]),
                (new_node[0] + 1, new_node[1]),
                (new_node[0], new_node[1] - 1),
                (new_node[0], new_node[1] + 1),
            ]

            for new_node in neighbors:
                if new_node in targets:
                    heapq.heappush(queue, (steps + 1, new_node))
                    targets.remove(new_node)
                    matrix[new_node[0]][new_node[1]] = steps + 1

        return matrix
