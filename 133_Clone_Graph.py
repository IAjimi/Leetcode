class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        """
        Runtime: 40 ms, faster than 83.75% of Python3 online submissions for Clone Graph.
        Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
        """
        if not node:
            return None

        queue = [node]
        new_nodes = {}

        while queue:
            node = queue.pop()
            if not node or node.val in new_nodes:
                continue

            # create node copy
            node_copy = Node(val=node.val)
            new_nodes[node.val] = node_copy

            for nn in node.neighbors:
                # undirected graph so we only need to edit links 1x
                if nn.val in new_nodes:
                    new_nodes[nn.val].neighbors.append(node_copy)
                    node_copy.neighbors.append(new_nodes[nn.val])
                else:
                    queue.append(nn)

        return new_nodes[1]
