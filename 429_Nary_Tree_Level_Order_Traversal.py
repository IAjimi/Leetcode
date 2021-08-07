"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        Runtime: 52 ms, faster than 68.27% of Python3 online submissions.
        Memory Usage: 16.1 MB, less than 61.08% of Python3 online submissions.
        """
        if not root:
            return []
        else:
            solution = [[]]
            queue = [(0, root)]

            while queue:
                level, node = queue.pop()

                if len(solution) < level + 1:  # this is fine bc we are going to explore in order
                    solution.append([])

                solution[level].append(node.val)

                if node.children:
                    for child in reversed(node.children):  # so we can .pop() instead of .pop(0)
                        queue.append((level + 1, child))

            return solution
