from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Runtime: 24 ms, faster than 95.46% of Python3 online submissions.
        Memory Usage: 14.4 MB, less than 28.76% of Python3 online submissions
        """
        first_tree = self.explore(p, path=[])
        second_tree = self.explore(q, path=[])
        return first_tree == second_tree

    def explore(self, node: TreeNode, path=[]):
        if node:
            path.append(node.val)
            self.explore(node.left, path)
            self.explore(node.right, path)
        else:
            path.append(None)

        return path

    def recursiveIsSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Runtime: 39 ms, faster than 56.22% of Python3 online submissions for Same Tree.
        Memory Usage: 14 MB, less than 59.70% of Python3 online submissions for Same Tree.
        """
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False

        # has nodes
        if p.val != q.val:
            return False

        if p.left and q.left:
            is_match_left = self.isSameTree(p.left, q.left)
        else:
            is_match_left = p.left == q.left

        if p.right and q.right:
            is_match_right = self.isSameTree(p.right, q.right)
        else:
            is_match_right = p.right == q.right

        return is_match_left and is_match_right
