from typing import List


class KruskalAlgorithm:

    def __init__(self):
        self.parents = []

        for i in range(0, 100):
            self.parents.append(i)

    def find_parents(self, x):
        if self.parents[x] == x:
            return x
        return self.find_parents(self.parents[x])

    def join(self, x, y):
        find_x = self.find_parents(x)
        find_y = self.find_parents(y)
        self.parents[find_x] = find_y


class Pairs:

    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def __str__(self):
        return f"{str(self.a)} -> {str(self.b)} weight: {str(self.w)}"


def read_from_file():
    edges: List[Pairs] = []
    file = open("graph.txt", "rt")

    for line in file:
        a, b, w = line.split()
        edges.append(Pairs(a, b, w))
    file.close()
    return edges


def read_from_stdin(edges_num):
    edges: List[Pairs] = []
    for i in range(edges_num):
        a, b, w = input().split()
        edges.append(Pairs(a, b, w))
    return edges


if __name__ == '__main__':

    algorithm = KruskalAlgorithm()

    number_of_vertices = int(input('Please enter the number of vertices: '))
    number_of_edges = int(input('Please enter the number of edge: '))

    choose_input = int(input("Choose '1' if you want to load graph.txt,\n\t"
                             "   '2' you want to enter graph from stdin \n"))

    edges_list = read_from_file() if choose_input == 1 else read_from_stdin(number_of_edges)

    edges_list = sorted(edges_list, key=lambda weight: weight.w)

    mEdges = 0
    mNi = 0

    while mEdges < number_of_vertices - 1 or mNi < number_of_edges:
        a = int(edges_list[mEdges].a)
        b = int(edges_list[mNi].b)
        w = int(edges_list[mNi].w)

        if algorithm.find_parents(a) != algorithm.find_parents(b):
            algorithm.join(a, b)
            print(a, " -> ", b, " weight: ", w)
            mEdges += 1

        mNi += 1
