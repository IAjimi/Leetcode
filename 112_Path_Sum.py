# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def __init__(self):
		self.found_sum = False

	def hasPathSum(self, root: TreeNode, targetSum: int, _sum=0) -> bool:
		"""
		Runtime: 44 ms, faster than 61.40% of Python3 online submissions.
		Memory Usage: 16 MB, less than 16.01% of Python3 online submissions.
		"""
		if root:
			_sum += root.val

			if _sum == targetSum and not root.left and not root.right:
				self.found_sum = True

			if root.left:
				self.hasPathSum(root.left, targetSum, _sum)

			if root.right:
				self.hasPathSum(root.right, targetSum, _sum)

		return self.found_sum
