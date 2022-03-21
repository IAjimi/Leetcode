from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 128 ms, faster than 59.80% of Python3 online submissions for All Paths From Source to Target.
        Memory Usage: 15.9 MB, less than 14.97% of Python3 online submissions for All Paths From Source to Target.
        """
        q = [(0, [])]
        all_paths = []

        while q:
            node, path = q.pop()

            path.append(node)

            if node == len(graph) - 1:
                all_paths.append(path)
                continue

            neighbors = graph[node]
            for n in neighbors:
                q.append((n, path.copy()))

        return all_paths
