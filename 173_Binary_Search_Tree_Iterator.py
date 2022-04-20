# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        Runtime: 122 ms, faster than 25.45% of Python3 online submissions for Binary Search Tree Iterator.
        Memory Usage: 19.9 MB, less than 90.96% of Python3 online submissions for Binary Search Tree Iterator.
        """
        self.tree = []
        self.pointer = 0
        self.explore(root)  # populate tree

    def explore(self, root: Optional[TreeNode]):
        if not root:
            return

        self.explore(root.left)
        self.tree.append(root.val)
        self.explore(root.right)

    def next(self) -> int:
        val = self.tree[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        return self.pointer < len(self.tree)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
