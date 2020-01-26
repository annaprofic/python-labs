import time
from typing import List


class Edges:

    def __init__(self, a, b, w):
        """
        Initialization of params with are representing Edge of graph.
        :param a: the first vertex
        :param b: the second vertex
        :param w: the weight of edge between them
        """
        self.a = a
        self.b = b
        self.weight = w

    def __repr__(self):
        return f"Edge({str(self.a)}, {str(self.b)}, {str(self.weight)})"

    def __str__(self):
        return f"{str(self.a)} - {str(self.b)} weight: {str(self.weight)}"


class KruskalAlgorithm:

    def __init__(self, file_name='graph.txt'):
        """
        Method load sorted graph, extract number of vertices and edges and create array of parents.
        :param file_name: the name of file with is contain graph
        """
        self.graph: List[Edges] = []
        self.number_of_vertices, self.number_of_edges = self.load_graph(file_name)
        self.parents = self.load_dependency()

    def load_graph(self, file):
        """
        Method loads graph and creat List of Edges, sort it by weight and count vertices and edges.
        :param file: file name to load graph from (graph.txt by default)
        :return: the number of vertices, number of edges
        """
        file = open(file, "rt")
        vertices = set()

        for line in file:
            a, b, weight = (line.split())
            self.graph.append(Edges(int(a), int(b), int(weight)))
            vertices.add(a), vertices.add(b)

        file.close()
        self.graph.sort(key=lambda w: w.weight)
        return len(vertices), len(self.graph)

    def load_dependency(self):
        """
        Method to fill array of parents with is representing dependency between vertices.
        :return: List comprehension from 0 to number of vertices.
        """
        return [vertex for vertex in range(self.number_of_vertices + 1)]

    def find_parents(self, x):
        """
        Method to find if vertices have the same parents
        :param x: graph vertex
        :return: the vertex that is linked input vertex
        """
        if self.parents[x] == x:
            return x
        return self.find_parents(self.parents[x])

    def join(self, x, y):
        """
        Method to join vertices if they haven't the same parents,
        in that way one of them is a parent of another one.
        :param x: the first vertex
        :param y: the second vertex
        """
        find_x, find_y = self.find_parents(x), self.find_parents(y)
        if find_x != find_y:
            self.parents[find_x] = find_y

    def run(self):
        """
        Main method to execute algorithm.
        :return: Minimum spanning tree for input graph
        """
        min_spanning_tree: List[Edges] = []

        for edge in range(len(self.graph)):
            a = int(self.graph[edge].a)
            b = int(self.graph[edge].b)
            weight = int(self.graph[edge].weight)

            # check if two vertices can create a cycle and if they can't - join them
            if algorithm.find_parents(a) != algorithm.find_parents(b):
                algorithm.join(a, b)
                min_spanning_tree.append(Edges(a, b, weight))

        return min_spanning_tree


if __name__ == '__main__':
    algorithm = KruskalAlgorithm()

    print('\nLoaded graph:\n')
    [print(str(algorithm.graph[edge])) for edge in range(len(algorithm.graph))]

    # run algorithm and get minimum spanning tree and check time
    t1 = time.perf_counter()
    minimum_spanning_tree: List[Edges] = algorithm.run()
    t2 = time.perf_counter()
    time_diff = t2 - t1

    print(f'\nMinimum spanning tree found with Kruskal Algorithm in {time_diff:.5f} secs:\n')
    [print(str(minimum_spanning_tree[edge])) for edge in range(len(minimum_spanning_tree))]
