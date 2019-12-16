import unittest
from lab10.queue.main import Queue


class TestMain(unittest.TestCase):

    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

        for i in range(10):
            self.queue1.put(i)

        self.queue2.put(1)
        self.queue2.put(2)
        self.queue2.put(3)
        self.queue_empty = Queue()

    def push_elements(self):
        self.queue2.put(77)
        self.queue2.put(99)
        self.queue_empty.put(1)
        self.queue_empty.put(2)
        self.queue_empty.put(3)
        self.queue_empty.put(4)
        self.queue_empty.put(5)

    def test__str__(self):
        self.assertEqual('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', str(self.queue1))
        self.assertEqual('[1, 2, 3]', str(self.queue2))
        self.assertEqual('[]', str(self.queue_empty))

    def test_is_empty(self):
        self.assertTrue(self.queue_empty.is_empty())
        self.assertFalse(self.queue1.is_empty())
        self.assertFalse(self.queue2.is_empty())

    def test_is_full(self):
        self.assertTrue(self.queue1.is_full())
        self.assertFalse(self.queue2.is_full())
        self.assertFalse(self.queue_empty.is_full())

    def test_push(self):
        self.push_elements()
        self.assertEqual('[1, 2, 3, 77, 99]', str(self.queue2))
        self.assertEqual('[1, 2, 3, 4, 5]', str(self.queue_empty))

    def test_pop(self):
        self.push_elements()
        self.queue2.get()
        self.queue2.get()
        self.queue_empty.get()
        self.queue_empty.get()
        self.queue_empty.get()
        self.assertEqual('[3, 77, 99]', str(self.queue2))
        self.assertEqual('[4, 5]', str(self.queue_empty))


if __name__ == '__main__':
    unittest.main()
