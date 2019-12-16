import unittest
from lab10.random_queue.main import RandomQueue


class TestMain(unittest.TestCase):

    def setUp(self):
        self.queue1 = RandomQueue()
        self.queue2 = RandomQueue()

        for i in range(10):
            self.queue1.insert(i)

        self.queue2.insert(1)
        self.queue2.insert(2)
        self.queue2.insert(3)
        self.queue_empty = RandomQueue()

    def test__str__(self):
        self.assertEqual('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', str(self.queue1))
        self.assertEqual('[1, 2, 3]', str(self.queue2))
        self.assertEqual('[]', str(self.queue_empty))

    def insert_elements(self):
        self.queue2.insert(77)
        self.queue2.insert(99)
        self.queue_empty.insert(1)
        self.queue_empty.insert(2)
        self.queue_empty.insert(3)
        self.queue_empty.insert(4)
        self.queue_empty.insert(5)

    def test_is_empty(self):
        self.assertTrue(self.queue_empty.is_empty())
        self.assertFalse(self.queue1.is_empty())
        self.assertFalse(self.queue2.is_empty())

    def test_is_full(self):
        self.assertTrue(self.queue1.is_full())
        self.assertFalse(self.queue2.is_full())
        self.assertFalse(self.queue_empty.is_full())

    def test_insert(self):
        self.insert_elements()
        self.assertEqual('[1, 2, 3, 77, 99]', str(self.queue2))
        self.assertEqual('[1, 2, 3, 4, 5]', str(self.queue_empty))

    def test_remove(self):
        self.insert_elements()
        self.queue2.remove()
        self.queue2.remove()
        self.queue_empty.remove()
        self.queue_empty.remove()
        self.queue_empty.remove()
        self.assertEqual(3, len(self.queue2))
        self.assertEqual(2, len(self.queue_empty))


if __name__ == '__main__':
    unittest.main()
