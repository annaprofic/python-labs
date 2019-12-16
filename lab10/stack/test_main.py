import unittest
from lab10.stack.main import Stack


class TestMain(unittest.TestCase):

    def setUp(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

        for i in range(10):
            self.stack1.push(i)

        self.stack2.push(1)
        self.stack2.push(2)
        self.stack2.push(3)
        self.stack_empty = Stack()

    def push_elements(self):
        self.stack2.push(77)
        self.stack2.push(99)
        self.stack_empty.push(1)
        self.stack_empty.push(2)
        self.stack_empty.push(3)

    def test__str__(self):
        self.assertEqual('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', str(self.stack1))
        self.assertEqual('[1, 2, 3]', str(self.stack2))
        self.assertEqual('[]', str(self.stack_empty))

    def test_is_empty(self):
        self.assertTrue(self.stack_empty.is_empty())
        self.assertFalse(self.stack1.is_empty())
        self.assertFalse(self.stack2.is_empty())

    def test_is_full(self):
        self.assertTrue(self.stack1.is_full())
        self.assertFalse(self.stack2.is_full())
        self.assertFalse(self.stack_empty.is_full())

    def test_push(self):
        self.push_elements()
        self.assertEqual('[1, 2, 3, 77, 99]', str(self.stack2))
        self.assertEqual('[1, 2, 3]', str(self.stack_empty))

    def test_pop(self):
        self.push_elements()
        self.stack2.pop()
        self.stack2.pop()
        self.stack_empty.pop()
        self.stack_empty.pop()
        self.stack_empty.pop()
        self.test__str__()


if __name__ == '__main__':
    unittest.main()

