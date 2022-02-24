# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 36 ms, faster than 83.53% of Python3 online submissions for Binary Tree Level Order Traversal.
        Memory Usage: 14.2 MB, less than 94.90% of Python3 online submissions for Binary Tree Level Order Traversal.
        """
        if not root:
            return []

        path = []
        queue = [(0, root)]

        while queue:
            level, node = queue.pop(0)

            if not node:
                continue
            else:
                if len(path) <= level:
                    path.append([node.val])
                else:
                    path[level].append(node.val)

            queue.append((level + 1, node.left))
            queue.append((level + 1, node.right))

        return path
