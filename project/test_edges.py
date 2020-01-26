import unittest
from project.kruskal_algorithm import Edges


class TestEdges(unittest.TestCase):

    def setUp(self):
        self.edge1 = Edges(1, 2, 3)
        self.edge2 = Edges(10, 7, 5)
        self.edge3 = Edges(0, 1, 4)

    def test___str__(self):
        self.assertEqual("1 - 2 weight: 3", str(self.edge1))
        self.assertEqual("10 - 7 weight: 5", str(self.edge2))
        self.assertEqual("0 - 1 weight: 4", str(self.edge3))

    def test___repr__(self):
        self.assertEqual("Edge(1, 2, 3)", repr(self.edge1))
        self.assertEqual("Edge(10, 7, 5)", repr(self.edge2))
        self.assertEqual("Edge(0, 1, 4)", repr(self.edge3))

    def tearDown(self):
        self.edge1 = None
        self.edge2 = None
        self.edge3 = None


if __name__ == '__main__':
    unittest.main()
