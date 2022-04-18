# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nodes = []

    def explore(self, root):
        if not root:
            return

        self.explore(root.left)
        self.nodes.append(root)
        self.explore(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        Runtime: 29 ms, faster than 91.75% of Python3 online submissions for Increasing Order Search Tree.
        Memory Usage: 14 MB, less than 50.58% of Python3 online submissions for Increasing Order Search Tree.
        """
        self.explore(root)
        self.nodes.append(None)

        for i, node in enumerate(self.nodes):
            if node:
                node.left = None
                node.right = self.nodes[i + 1]

        return self.nodes[0]
