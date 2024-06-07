class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def deleteNode(self, data):
        print("Deleting {}".format(data))
        current = self.head
        if current.data == data:
            self.head = current.next
        else:
            while current and current.data != data:
                current = current.next
            if current is not None:
                print("{} found.".format(data))
                previous = self.head
                while previous.next != current:
                    previous = previous.next
                previous.next = current.next
            else:
                print("{} not found.".format(data))

    def displayLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next