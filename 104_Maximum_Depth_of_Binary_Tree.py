from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        """
        Runtime: 56 ms, faster than 48.98% of Python3 online submissions for Maximum Depth of Binary Tree.
        Memory Usage: 16.4 MB, less than 8.18% of Python3 online submissions for Maximum Depth of Binary Tree.
        """
        if not root:
            return depth

        depth += 1
        left_depth = self.maxDepth(root.left, depth) if root.left else depth
        right_depth = self.maxDepth(root.right, depth) if root.right else depth

        return max(left_depth, right_depth)

