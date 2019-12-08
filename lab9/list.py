class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __str__(self):
        i = self.head
        str_list = []
        while i is not None:
            str_list.append(i.data)
            i = i.next
        return str(str_list)

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("can't remove head, list is empty.")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.length == 0:
            raise ValueError("can't remove tail, list is empty.")
        node = self.tail
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            i = self.head
            while i.next != self.tail:
                i = i.next
            self.tail = i
            self.tail.next = i.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):
        if not isinstance(other, SingleList) or other.length == 0:
            raise ValueError("'other' list has to be SingleList instance and have at least one Node.")
        if self.length == 0:
            self.head = other.head
            self.tail = other.tail
        if self.head == self.tail:
            self.head.next = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.length
        return self

    def clear(self):
        self.head = self.tail = None
        self.length = 0
        return self


if __name__ == '__main__':

    list1, list2 = SingleList(), SingleList()

    def make_first_list(list1):
        for i in range(1, 5):
            list1.insert_head(Node(i))
        list1.insert_tail(Node(0))  # 4, 3, 2, 1, 0


    def make_second_list(list2):
        for i in range(11, 15):
            list2.insert_head(Node(i))
        list2.insert_tail(Node(10))  # 4, 3, 2, 1, 0


    make_first_list(list1)
    
    list1.remove_tail()  # 4, 3, 2, 1
    assert list1.tail.data == 1
    list1.remove_tail()  # 4, 3, 2
    assert list1.tail.data == 2
    list1.remove_tail()  # 4, 3
    assert list1.tail.data == 3
    list1.remove_tail()  # 4
    assert list1.tail.data == 4
    list1.remove_tail()
    assert list1.tail is None and list1.length == 0

    make_first_list(list1)
    make_second_list(list2)
    assert str(list1.merge(list2)) == "[4, 3, 2, 1, 0, 14, 13, 12, 11, 10]" and list1.length == 10

    list1.clear()
    list2.clear()
    assert list1.is_empty() is True and list2.is_empty() is True

    make_first_list(list1)
    make_second_list(list2)
    assert str(list2.merge(list1)) == "[14, 13, 12, 11, 10, 4, 3, 2, 1, 0]" and list2.length == 10
