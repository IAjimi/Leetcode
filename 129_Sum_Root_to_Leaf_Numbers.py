# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._sum = 0

    def sumNumbers(self, root: TreeNode, path="") -> int:
        """
        Runtime: 32 ms, faster than 64.60% of Python3 online submissions.
        Memory Usage: 14.3 MB, less than 49.30% of Python3 online submissions."""
        path += str(root.val)

        if not root.left and not root.right:
            self._sum += int(path)

        if root.left:
            self.sumNumbers(root.left, path)
        if root.right:
            self.sumNumbers(root.right, path)

        return self._sum
