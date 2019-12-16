class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return len(self.items) >= 10

    def push(self, item):
        if self.is_full():
            raise IndexError("Your stack is full.")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Your stack is empty.")
        return self.items.pop()
