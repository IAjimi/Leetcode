from typing import List, Tuple


class Solution:
    def bfs(
        self, start: Tuple[int, int], isConnected: List[List[int]]
    ) -> List[List[int]]:
        q = [(start)]

        while q:
            (i, j) = q.pop()

            if not (0 <= i < len(isConnected)) or not (0 <= j < len(isConnected[0])):
                continue
            elif isConnected[i][j] == 0:
                continue

            isConnected[i][j] = 0
            isConnected[j][i] = 0

            neighbors = [
                (j, i) for j in range(len(isConnected[i])) if isConnected[i][j] == 1
            ]
            for n in neighbors:
                q.append(n)

        return isConnected

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Runtime: 638 ms, faster than 5.01% of Python3 online submissions for Number of Provinces.
        Memory Usage: 31.7 MB, less than 5.13% of Python3 online submissions for Number of Provinces.
        """
        count = 0

        for i in range(len(isConnected)):
            if isConnected[i][i] == 1:
                isConnected = self.bfs((i, i), isConnected)
                count += 1

        return count
