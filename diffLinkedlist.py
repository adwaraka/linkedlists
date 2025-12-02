from typing import Optional

class Node(object):

    def __init__(self, data: int):
        self.data = data
        self.pointer: Optional['Node'] = None


class SingleLinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data:int) -> None:
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            current = self.head
            while current.pointer:
                current = current.pointer
            newNode = Node(data)
            current.pointer = newNode

    def convert(self) -> int:
        n, value = 0, 0
        current = self.head
        while current:
            # print(current.data)
            # print
            value+=current.data*pow(10, n)
            n+=1
            current = current.pointer
        return value


s = SingleLinkedList()
s.insert(3)
s.insert(1)
s.insert(5)
s.insert(7)
print(s.convert())