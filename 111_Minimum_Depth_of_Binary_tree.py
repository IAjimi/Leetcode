# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """Top 70% by speed, top 30% by memory."""
    def minDepth(self, root):
        if root:
            n = self.explore(root, 1)
            return n
        else:
            return 0

    def explore(self, root, n):
        if not root.left and not root.right:
            return n

        left_n = self.explore(root.left, n + 1) if root.left else 100000
        right_n = self.explore(root.right, n + 1) if root.right else 100000

        return min(left_n, right_n)