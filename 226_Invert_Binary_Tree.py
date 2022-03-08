# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 41 ms, faster than 54.16% of Python3 online submissions for Invert Binary Tree.
        Memory Usage: 13.9 MB, less than 65.92% of Python3 online submissions for Invert Binary Tree.
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
