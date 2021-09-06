# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Runtime: 28 ms, faster than 99.59% of Python3 online submissions.
    Memory Usage: 16.1 MB, less than 61.37% of Python3 online submissions.
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return self.explore(root, 1)
        else:
            return 0
    
    def explore(self, root, n):        
        if not root or (not root.left and not root.right):
            return n

        left_n = self.explore(root.left, n + 1)
        right_n = self.explore(root.right, n + 1)
        return max(left_n, right_n)
