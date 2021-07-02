# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def __init__(self):
		self.path = []

	def levelOrder(self, root):
		"""BFS approach.

		Runtime: 32 ms, faster than 84.13% of Python3 online submissions.
		Memory Usage: 14.4 MB, less than 87.06% of Python3 online submissions.
		"""
		visited = []

		if root:
			queue = [(root, 1)]

			while queue:
				element, level = queue.pop(0)
				if len(visited) < level:
					visited.append([element.val])
				else:
					visited[level - 1].append(element.val)

				if element.left:
					queue.append((element.left, level + 1))
				if element.right:
					queue.append((element.right, level + 1))

		return visited

	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		"""
		Input [3,9,20,null,null,15,7]
		Output
		[[3,9,20,15,7]]
		Expected
		[[3],[9,20],[15,7]]"""
		self.path.append(root.val)
		if root.left:
			self.levelOrder(root.left)
		if root.right:
			self.levelOrder(root.right)
		return [self.path]