import heapq


class Solution:
	def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
		"""
		Runtime: 752 ms, faster than 51.28% of Python3 online submissions.
		Memory Usage: 17.4 MB, less than 42.63% of Python3 online submissions.

		BFS.
		* list of zeroes (position)
		* move outwards from every zero, keep next nodes in min heap
		* populate old matrix with updated distances
		* terminate when all nodes have been "visited"
		"""
		# Fill queue
		targets = set()
		queue = []
		for ix in range(len(matrix)):
			for jx in range(len(matrix[0])):
				if matrix[ix][jx] == 0:
					heapq.heappush(queue, (0, (ix, jx)))
				else:
					targets.add((ix, jx))

		while targets:
			steps, new_node = heapq.heappop(queue)

			neighbors = [(new_node[0] - 1, new_node[1]),
						 (new_node[0] + 1, new_node[1]),
						 (new_node[0], new_node[1] - 1),
						 (new_node[0], new_node[1] + 1)]

			for new_node in neighbors:
				if new_node in targets:
					heapq.heappush(queue, (steps + 1, new_node))
					targets.remove(new_node)
					matrix[new_node[0]][new_node[1]] = steps + 1

		return matrix

	def manhattanDistance(self, p1, p2):
		return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

	def alt_updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
		"""
		Too slow because computes the Manhattan distance for ALL zeros in the matrix.
		"""
		zero_list = [(ix, jx) for ix in range(len(matrix)) for jx in range(len(matrix[0])) if matrix[ix][jx] == 0]

		for ix in range(len(matrix)):
			for jx in range(len(matrix[0])):
				if matrix[ix][jx] == 1:
					distance = [self.manhattanDistance((ix, jx), zero) for zero in zero_list]
					matrix[ix][jx] = min(distance)

		return matrix


