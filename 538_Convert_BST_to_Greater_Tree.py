# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def explore(self, root, prev_val=0):
        if not root:
            return prev_val

        root.val += self.explore(root.right, prev_val)
        return self.explore(root.left, root.val)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 145 ms, faster than 20.81% of Python3 online submissions for Convert BST to Greater Tree.
        Memory Usage: 16.7 MB, less than 77.23% of Python3 online submissions for Convert BST to Greater Tree.
        """
        self.explore(root, 0)
        return root
