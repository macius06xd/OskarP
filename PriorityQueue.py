class PriorityQueue:
    def __init__(self):
        # each element should be stored as a tuple (item,priority)
        # each should be sorted based on priority
        self.items = []

    def is_empty(self):
        # Returns True if the priority queue is empty, False otherwise
        pass

    def size(self):
        # Returns the number of elements in the priority queue
        pass

    def enqueue(self, item, priority):
        # Inserts an item into the priority queue based on its priority
        item_to_insert = (item,priority)
        pass

    def dequeue(self):
        # Removes and returns the item with the highest priority from the queue
        pass

    def peek(self):
        # Returns the item with the highest priority without removing it
        pass
