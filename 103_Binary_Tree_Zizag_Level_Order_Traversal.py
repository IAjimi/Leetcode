# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 65 ms, faster than 11.23% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
        Memory Usage: 14.1 MB, less than 83.81% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
        """
        queue = deque([(0, root)])
        path = []

        while queue:
            level, node = queue.popleft()
            if not node:
                continue

            # add to path
            if len(path) <= level:
                path.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    path[level].append(node.val)
                else:
                    path[level].appendleft(node.val)

            # queue next level
            level += 1

            queue.append((level, node.left))
            queue.append((level, node.right))

        return path
