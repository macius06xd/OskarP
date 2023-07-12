import unittest

from PriorityQueue import PriorityQueue


class PriorityQueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('A', 1)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(0, self.queue.size())
        self.queue.enqueue('A', 1)
        self.assertEqual(1, self.queue.size())
        self.queue.enqueue('B', 2)
        self.assertEqual(2, self.queue.size())
        self.queue.dequeue()
        self.assertEqual(1, self.queue.size())

    def test_enqueue(self):
        self.queue.enqueue('A', 1)
        self.assertEqual('A', self.queue.peek())
        self.queue.enqueue('B', 3)
        self.assertEqual('A', self.queue.peek())
        self.queue.enqueue('C', 2)
        self.assertEqual('A', self.queue.peek())

    def test_dequeue(self):
        self.queue.enqueue('A', 1)
        self.queue.enqueue('B', 3)
        self.queue.enqueue('C', 2)
        self.assertEqual('B', self.queue.dequeue())
        self.assertEqual('C', self.queue.dequeue())
        self.assertEqual('A', self.queue.dequeue())

    def test_peek(self):
        self.queue.enqueue('A', 1)
        self.assertEqual('A', self.queue.peek())
        self.queue.enqueue('B', 3)
        self.assertEqual('A', self.queue.peek())
        self.queue.enqueue('C', 2)
        self.assertEqual('A', self.queue.peek())

if __name__ == '__main__':
    unittest.main()