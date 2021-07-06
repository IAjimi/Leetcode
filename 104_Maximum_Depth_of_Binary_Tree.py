# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """Top 60% by speed", top 70% by memory."""
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            n = self.explore(root, 1)
            return n
        else:
            return 0
    
    def explore(self, root, n):        
        if not root or (not root.left and not root.right):
            return n

        left_n, right_n = 0, 0
        left_n = self.explore(root.left, n + 1)
        right_n = self.explore(root.right, n + 1)
        
        return max(left_n, right_n)
        