from typing import List


# class which is representing edge between vertices
class Edges:

    # initializing vertex a and vertex b which are joined with w - weight
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.weight = w

    def __str__(self):
        return f"{str(self.a)} - {str(self.b)} weight: {str(self.weight)}"


# class contains necessary methods of algorithm
class KruskalAlgorithm:

    def __init__(self, file_name='graph.txt'):
        self.parents = []
        self.graph: List[Edges] = []
        self.number_of_vertices = 0

        self.graph, self.number_of_vertices = self.load_graph(file_name)
        self.parents = self.load_dependency()
        self.number_of_edges = len(self.graph)

        # sorting graph by weight (key = weight) by system method
        self.graph = sorted(self.graph, key=lambda w: w.weight)

        # load array of parents

    # load graph from graph.txt file by default and fill array of vertices
    def load_graph(self, file):
        file = open(file, "rt")
        vertices = set()

        # create graph data structure with vertex 1 (a) vertex 2 (b) and weight
        for line in file:
            a, b, weight = line.split()
            vertices.add(a)
            vertices.add(b)
            self.graph.append(Edges(a, b, weight))
        file.close()
        return self.graph, len(vertices)

    # method to fill array of parents with is representing dependency between vertices
    def load_dependency(self):
        for vertex in range(0, self.number_of_vertices + 1):
            self.parents.append(vertex)
        return self.parents

    # method to find if vertices have the same parents
    def find_parents(self, x):
        if self.parents[x] == x:
            return x
        return self.find_parents(self.parents[x])

    # join vertices if they haven't same parents, than one of them is parent of other one
    def join(self, x, y):
        find_x = self.find_parents(x)
        find_y = self.find_parents(y)
        self.parents[find_x] = find_y

    def run(self):
        min_spanning_tree: List[Edges] = []
        vertex1 = 0
        vertex2 = 0

        while vertex1 < self.number_of_vertices - 1 or vertex2 < self.number_of_edges:
            a = int(self.graph[vertex2].a)
            b = int(self.graph[vertex2].b)
            weight = int(self.graph[vertex2].weight)

            # check if vertices have the same parents and if yes you can join them
            if algorithm.find_parents(a) != algorithm.find_parents(b):
                algorithm.join(a, b)
                min_spanning_tree.append(Edges(a, b, weight))
                vertex1 += 1
            vertex2 += 1

        return min_spanning_tree


if __name__ == '__main__':

    algorithm = KruskalAlgorithm()

    print('\nLoaded graph:\n')

    for edge in range(len(algorithm.graph)):
        print(str(algorithm.graph[edge]))

    # run algorithm and get minimum spanning tree
    minimum_spanning_tree: List[Edges] = algorithm.run()

    print('\nMinimum spanning tree found with Kruskal Algorithm:\n')
    for edge in range(len(minimum_spanning_tree)):
        print(str(minimum_spanning_tree[edge]))
