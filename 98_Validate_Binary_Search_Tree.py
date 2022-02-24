from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], _min=-(10**12), _max=10**12
    ) -> bool:
        """
        Runtime: 44 ms, faster than 89.68% of Python3 online submissions for Validate Binary Search Tree.
        Memory Usage: 16.6 MB, less than 37.42% of Python3 online submissions for Validate Binary Search Tree.
        """
        if not root:
            return True

        if root.val <= _min or root.val >= _max:
            return False

        is_left_bst_valid = self.isValidBST(root.left, _max=root.val, _min=_min)
        is_right_bst_valid = self.isValidBST(root.right, _min=root.val, _max=_max)

        return is_left_bst_valid and is_right_bst_valid
