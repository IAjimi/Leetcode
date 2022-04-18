# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        """
        Key is to realize that, given BST properties, the root being too small invalidates
        the whole left subtree, and the root being too large invalidates the whole right
        subtree.

        Runtime: 48 ms, faster than 95.89% of Python3 online submissions for Trim a Binary Search Tree.
        Memory Usage: 18 MB, less than 48.91% of Python3 online submissions for Trim a Binary Search Tree.
        """
        if not root:
            return
        # too small, only consider right subtree
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        # too big, only consider left subtree
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        # fine, recursively trim subtrees
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
