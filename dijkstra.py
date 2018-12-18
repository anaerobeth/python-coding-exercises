"""
Find the shortest distance between two nodes
Adapted from: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

Steps:
1. Create a list of unvisited nodes
2. Set distance 0 for start node, Inf for the rest
3. Find distance of neighbors from current node and save if smaller
4. Remove node from unvisited list
5. Stop if destination node, or smallest distance between unvisited nodes is Inf.
If not repeat from step 3

"""

from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


class Graph:

    def __init__(self, edges):
        self.edges = [self.make_edge(*edge) for edge in edges]
        all_edges = [[edge.start, edge.end] for edge in self.edges]
        self.nodes = [item for sublist in all_edges for item in sublist]
        self.neighbors = {node: set() for node in self.nodes}
        for edge in self.edges:
            self.neighbors[edge.start].add((edge.end, edge.cost))


    def make_edge(self, start, end, cost=1):
        return Edge(start, end, cost)


    def dijkstra(self, source, dest):

        """
        >>> graph = Graph([
        ... ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
        ... ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
        ... ("e", "f", 9)])
        >>> graph.dijkstra("a", "e")
        ['a', 'c', 'd', 'e']
        """

        distances = {node: inf for node in self.nodes}
        path_nodes = {node: None for node in self.nodes}
        distances[source] = 0
        visited = self.nodes.copy()

        while visited:
            current = min(visited, key=lambda node: distances[node])
            visited.remove(current)

            # Stop when the minimum distance is Inf
            if distances[current] == inf:
                break
            for neighbor, cost in self.neighbors[current]:
                alt_route = distances[current] + cost
                if alt_route < distances[neighbor]:
                    distances[neighbor] = alt_route
                    path_nodes[neighbor] = current


        path = []
        while path_nodes[dest] is not None:
            path.append(dest)
            dest = path_nodes[dest]

        path.append(source)
        path.reverse()

        return path


if __name__ == '__main__':
    import doctest
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    log = logging.info
    doctest.testmod()
