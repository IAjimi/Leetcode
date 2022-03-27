from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """
        Runtime: 104 ms, faster than 55.13% of Python3 online submissions for Flood Fill.
        Memory Usage: 14 MB, less than 95.54% of Python3 online submissions for Flood Fill.
        """
        q = [(sr, sc)]
        initial_color = image[sr][sc]
        visited = set()

        while q:
            i, j = q.pop()

            if not (0 <= i <= len(image) - 1) or not (0 <= j <= len(image[0]) - 1):
                continue
            elif (i, j) in visited:
                continue
            elif image[i][j] != initial_color:
                continue

            visited.add((i, j))
            image[i][j] = newColor
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for n in neighbors:
                q.append(n)

        return image
