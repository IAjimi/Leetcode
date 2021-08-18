# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def __init__(self):
		self.counter = 0

	def goodNodes(self, root: TreeNode, cur_max=-10 ** 5) -> int:
		"""
		Runtime: 216 ms, faster than 99.30% of Python3 online submissions.
		Memory Usage: 33.2 MB, less than 70.13% of Python3 online submissions.
		"""
		if root.val >= cur_max:
			self.counter += 1
			cur_max = root.val

		if root.left: self.goodNodes(root.left, cur_max)
		if root.right: self.goodNodes(root.right, cur_max)

		return self.counter
