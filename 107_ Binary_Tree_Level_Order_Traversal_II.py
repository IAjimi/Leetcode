# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def levelOrderBottom(self, root):
		"""BFS approach. Same as 102, Binary Tree Level Order Traversal, but reversing order of list.

		Runtime: 28 ms, faster than 94.89% of Python3 online submissions.
		Memory Usage: 14.7 MB, less than 41.84% of Python3 online submissions.
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

		return visited[::-1]
