# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
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