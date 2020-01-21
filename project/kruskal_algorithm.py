from typing import List


# class contains necessary methods of algorithm
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


# class which is representing edge between vertices
class Edges:

    # initializing vertex a and vertex b which are joined with w - weight
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.weight = w

    def __str__(self):
        return f"{str(self.a)} <-> {str(self.b)} weight: {str(self.weight)}"


# method to load graph from file graph.txt
def read_from_file():
    # graph data structure is storing in List which is contain Edge instances
    loaded_graph: List[Edges] = []
    file = open("graph.txt", "rt")

    for line in file:
        a, b, weight = line.split()
        loaded_graph.append(Edges(a, b, weight))
    file.close()
    return loaded_graph


# method to load graph from standard input
def read_from_stdin(edges_num):
    loaded_graph: List[Edges] = []

    for i in range(edges_num):
        a, b, weight = input().split()
        loaded_graph.append(Edges(a, b, weight))
    return loaded_graph


if __name__ == '__main__':

    # loading number of vertices and number of edges from standard input
    number_of_vertices = int(input('Please enter the number of vertices: '))
    number_of_edges = int(input('Please enter the number of edge: '))

    algorithm = KruskalAlgorithm()

    choose_input = int(input("Choose '1' if you want to load graph.txt,\n\t"
                             "   '2' you want to enter graph from stdin \n"))

    # building graph data structure from file or from stdin
    graph = read_from_file() if choose_input == 1 else read_from_stdin(number_of_edges)

    # sorting graph by weight (key = weight) by system method
    graph = sorted(graph, key=lambda weight: weight.weight)

    vertex1 = 0
    vertex2 = 0

    while vertex1 < number_of_vertices - 1 or vertex2 < number_of_edges:
        a = int(graph[vertex2].a)
        b = int(graph[vertex2].b)
        weight = int(graph[vertex2].weight)

        if algorithm.find_parents(a) != algorithm.find_parents(b):
            algorithm.join(a, b)
            print(a, "<->", b, "weight:", weight)
            vertex1 += 1

        vertex2 += 1
