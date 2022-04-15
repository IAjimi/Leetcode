# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Runtime: 86 ms, faster than 75.40% of Python3 online submissions for Search in a Binary Search Tree.
        Memory Usage: 16.5 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.
        """
        if not root:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
