class Solution:
    def __init__(self):
        self.islands = []

    def numIslands(self, grid):
        """
        BFS with islands stored in a hash map for quick membership test + removal.

        Runtime: 152 ms, faster than 39.67% of Python3 online submissions for Number of Islands.
        Memory Usage: 19.1 MB, less than 18.52% of Python3 online submissions for Number of Islands.
        """
        self.islands = {
            (ix, jx): 1
            for ix in range(len(grid))
            for jx in range(len(grid[0]))
            if grid[ix][jx] == "1"
        }
        counter = 0

        while self.islands:
            self.explore()
            counter += 1

        return counter

    def explore(self):
        queue = [list(self.islands.keys())[0]]

        while queue and self.islands:
            node = queue.pop()
            if node in self.islands:
                del self.islands[node]

                ix, jx = node
                neighbors = [(ix + 1, jx), (ix - 1, jx), (ix, jx - 1), (ix, jx + 1)]

                for neighbor in neighbors:
                    if neighbor in self.islands:
                        queue.append(neighbor)


if __name__ == "__main__":
    assert 1 == Solution().numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )

    assert 3 == Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )

    assert 2 == Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )

    assert 1 == Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["0", "0", "1", "1", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )

    assert 3 == Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "0", "0", "0", "0"],
            ["0", "0", "1", "1", "0"],
            ["0", "0", "0", "0", "1"],
        ]
    )

    assert 0 == Solution().numIslands(
        grid=[
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
