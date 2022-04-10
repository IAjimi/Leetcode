from typing import List


class Solution:
    """
    Basically just a graph traversal problem.

    Runtime: 132 ms, faster than 38.94% of Python3 online submissions.
    Memory Usage: 19.2 MB, less than 36.06% of Python3 online submissions.
    """

    def __init__(self):
        self.visited = set()

    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0

        for node in nums:
            length = self.explore(node, nums)
            max_length = max(max_length, length)

        return max_length

    def explore(self, start: int, nums: List[int]) -> int:
        length, node = 1, start

        while len(self.visited) < len(nums):
            self.visited.add(node)
            next_node = nums[node]
            if next_node not in self.visited:
                length, node = length + 1, next_node
            else:
                return length

        return length
