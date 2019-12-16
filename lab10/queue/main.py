class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return len(self.items) == 10

    def put(self, data):
        if self.is_full():
            raise IndexError("The queue is full.")
        self.items.append(data)

    def get(self):
        if self.is_empty(): 
            raise IndexError("The queue is empty.")
        return self.items.pop(0)
