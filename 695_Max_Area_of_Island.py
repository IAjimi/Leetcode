from typing import List


class Solution:
	"""
	DFS. Get position of all 1s, then visit them 1 by 1.
	Runtime: 184 ms, faster than 19.24% of Python3 online submissions.
	Memory Usage: 15.2 MB, less than 73.13% of Python3 online submissions.
	"""
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		max_area = 0
		nodes = {(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 1}
		queue = list(nodes)

		while queue:
			n = queue.pop()
			area, recently_visited = self.explore(n, nodes)
			queue = [q for q in queue if q not in recently_visited]
			max_area = max(max_area, area)

		return max_area

	def neighbors(self, node: tuple) -> list[tuple]:
		"""
		Returns list of neighboring nodes.
		"""
		x, y = node
		return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

	def explore(self, start: tuple, nodes: set):
		"""
		DFS implementation.
		"""
		area = 0
		queue = [start]
		recently_visited = set()

		while queue:
			node = queue.pop()

			if node not in recently_visited:
				recently_visited.add(node)
				area += 1

				for n in self.neighbors(node):
					if n in nodes:
						queue.append(n)

		return area, recently_visited
