class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top: Node):
    if top is None:
        return 0
    if (top.right and top.left) is None:
        return 1
    if not isinstance(top, Node):
        raise ValueError("'top' has to be Node instance.")
    return count_leafs(top.left) + count_leafs(top.right)


def count_total(top: Node):  # przechodzenie i dodawanie typu preorder
    if top is not None:
        if not isinstance(top, Node):
            raise ValueError("'top' has to be Node instance.")
        return top.data + count_total(top.left) + count_total(top.right)
    return 0


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    assert count_leafs(root) == 4
    assert count_total(root) == 28
