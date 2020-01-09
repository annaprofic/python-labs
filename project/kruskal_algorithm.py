from typing import List


class KruskalAlgorithm:

    def __init__(self):
        self.parents = []

        for vertex in range(0, 100):
            self.parents.append(vertex)

    def find_parents(self, x):
        if self.parents[x] == x:
            return x
        return self.find_parents(self.parents[x])

    def join(self, x, y):
        find_x = self.find_parents(x)
        find_y = self.find_parents(y)
        self.parents[find_x] = find_y


class Edges:

    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.weight = w

    def __str__(self):
        return f"{str(self.a)} <-> {str(self.b)} weight: {str(self.weight)}"


def read_from_file():
    graph: List[Edges] = []
    file = open("graph.txt", "rt")

    for line in file:
        a, b, weight = line.split()
        graph.append(Edges(a, b, weight))
    file.close()
    return graph


def read_from_stdin(edges_num):
    graph: List[Edges] = []

    for i in range(edges_num):
        a, b, weight = input().split()
        graph.append(Edges(a, b, weight))
    return graph


if __name__ == '__main__':

    algorithm = KruskalAlgorithm()
    print(algorithm.parents)

    # loading number og vertices and number of edges from standard input
    number_of_vertices = int(input('Please enter the number of vertices: '))
    number_of_edges = int(input('Please enter the number of edge: '))

    choose_input = int(input("Choose '1' if you want to load graph.txt,\n\t"
                             "   '2' you want to enter graph from stdin \n"))

    # building graph data structure from file or from stdin
    graph = read_from_file() if choose_input == 1 else read_from_stdin(number_of_edges)

    # now we are soring graph by weight
    graph = sorted(graph, key=lambda weight: weight.weight)

    for i in graph:
        print(str(i) + "x")

    vertex1 = 0
    vertex2 = 0

    while vertex1 < number_of_vertices - 1 or vertex2 < number_of_edges:
        a = int(graph[vertex1].a)
        b = int(graph[vertex2].b)
        weight = int(graph[vertex2].weight)

        if algorithm.find_parents(a) != algorithm.find_parents(b):
            algorithm.join(a, b)
            print(a, "<->", b, "weight:", weight)
            vertex1 += 1

        vertex2 += 1
