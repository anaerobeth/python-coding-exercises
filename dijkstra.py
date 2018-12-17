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
    def vertices(self):
        all_edges = [[edge.start, edge.end] for edge in self.edges]
        return [item for sublist in all_edges for item in sublist]


    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours


    def dijkstra(self, source, dest):

        """
        >>> graph = Graph([
        ... ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
        ... ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
        ... ("e", "f", 9)])
        >>> graph.dijkstra("a", "e")
        deque(['a', 'c', 'd', 'e'])
        """

        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)

        return path


if __name__ == '__main__':
    import doctest
    doctest.testmod()
