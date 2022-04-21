# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.i = 0
        self.kth_min_val = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Runtime: 53 ms, faster than 84.52% of Python3 online submissions for Kth Smallest Element in a BST.
        Memory Usage: 17.9 MB, less than 90.88% of Python3 online submissions for Kth Smallest Element in a BST.
        """
        if not root:
            return root

        self.kthSmallest(root.left, k)

        self.i += 1
        if self.i == k:
            self.kth_min_val = root.val
            return root.val

        self.kthSmallest(root.right, k)

        return self.kth_min_val
