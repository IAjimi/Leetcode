from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Insight behind problem is we just need the logic to check if subtrees are mirrored:

            Example: is [5,7,8] == [5,8,7]?

            If the roots don't match, we know the subtree is different, so we can return False.
            Otherwise, we check the children: they are either in the same order (left = left, right = right)
            or flipped (left = right, right = left).

            Recursion allows us to elegantly extend this simple logic to the whole tree.

        Runtime: 47 ms, faster than 46.97% of Python3 online submissions for Flip Equivalent Binary Trees.
        Memory Usage: 13.9 MB, less than 93.24% of Python3 online submissions for Flip Equivalent Binary Trees.
        """
        if not root1 and not root2:
            return True
        elif (root1 and not root2) or (not root1 and root2):
            return False

        if root1.val != root2.val:
            return False

        is_same_og_order = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )
        is_same_flip_order = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )

        return is_same_og_order or is_same_flip_order
