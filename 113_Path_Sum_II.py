# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.valid_paths = []

    def stackPathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
        Runtime: 44 ms, faster than 76.98% of Python3 online submissions.
        Memory Usage: 15.1 MB, less than 97.78% of Python3 online submissions.
        """
        if not root:
            return []
        else:
            solution = []
            stack = [(0, root, [])]

            while stack:
                cur_sum, node, cur_path = stack.pop()
                cur_sum += node.val
                cur_path.append(node.val)

                # Reached target and is a leaf!
                if cur_sum == targetSum and not node.left and not node.right:
                    solution.append(cur_path[:])
                # Haven't reached target yet, keep exploring
                else:
                    if node.right:
                        stack.append((cur_sum, node.right, cur_path[:]))
                    if (
                        node.left
                    ):  # since popping from the end, we do left *after* right
                        stack.append((cur_sum, node.left, cur_path[:]))

            return solution

    def recursivePathSum(
        self, root: TreeNode, targetSum: int, _sum=0, path=None
    ) -> List[List[int]]:
        """
        Need to be careful with lists - identical code with path = [] led to bugs.

        Runtime: 52 ms, faster than 29.51% of Python3 online submissions.
        Memory Usage: 20 MB, less than 5.23% of Python3 online submissions.
        """
        if root:
            if not path:
                path = []
            path.append(root.val)
            _sum += root.val

            if _sum == targetSum and not root.left and not root.right:
                self.valid_paths.append(path.copy())

            if root.left:
                self.pathSum(root.left, targetSum, _sum, path.copy())

            if root.right:
                self.pathSum(root.right, targetSum, _sum, path.copy())

        return self.valid_paths
