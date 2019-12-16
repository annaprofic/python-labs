import random as rd


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def get_rand_item(self):
        index = rd.randint(0, self.__len__() - 1)
        return index, self.items[index]

    def insert(self, item):
        if self.is_full():
            raise IndexError("The random queue is full.")
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("The random queue is empty.")
        random_item, replaced = self.get_rand_item()
        self.items[random_item] = self.items[-1]
        del self.items[-1]
        return replaced

    def is_empty(self):
        return not self.items

    def is_full(self):
        return self.__len__() == 10

    def clear(self):
        self.items.clear()
