"""
Find the shortest distance between two nodes
Adapted from: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

Steps:
1. Create a list of unvisited nodes
2. Set distance 0 for start node, Inf for the resn
3. Find distance of neighbors from current node and save if smaller
4. Remove node from unvisited list
5. Stop if destination node, or smallest distance between unvisited nodes is Inf.
If not repeat from step 3

"""

from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:

    def __init__(self, edges):
        self.edges = [make_edge(*edge) for edge in edges]


    @property
    def nodes(self):
        all_edges = [[edge.start, edge.end] for edge in self.edges]
        return [item for sublist in all_edges for item in sublist]


    @property
    def neighbors(self):
        neighbors = {node: set() for node in self.nodes}
        for edge in self.edges:
            neighbors[edge.start].add((edge.end, edge.cost))

        return neighbors


    def dijkstra(self, source, dest):

        """
        >>> graph = Graph([
        ... ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
        ... ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
        ... ("e", "f", 9)])
        >>> graph.dijkstra("a", "e")
        deque(['a', 'c', 'd', 'e'])
        """

        distances = {node: inf for node in self.nodes}
        path_nodes = {node: None for node in self.nodes}
        distances[source] = 0
        nodes = self.nodes.copy()

        while nodes:
            current_node = min(
                nodes, key=lambda node: distances[node])
            nodes.remove(current_node)
            if distances[current_node] == inf:
                break
            for neighbor, cost in self.neighbors[current_node]:
                alternative_route = distances[current_node] + cost
                if alternative_route < distances[neighbor]:
                    distances[neighbor] = alternative_route
                    path_nodes[neighbor] = current_node

        path, current_node = deque(), dest
        while path_nodes[current_node] is not None:
            path.appendleft(current_node)
            current_node = path_nodes[current_node]
        if path:
            path.appendleft(current_node)

        return path


if __name__ == '__main__':
    import doctest
    doctest.testmod()
