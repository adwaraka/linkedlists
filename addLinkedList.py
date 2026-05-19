from typing import Optional

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None
      

class Linkedlist(object):
    def __init__(self):
        self.head = None
    
    def insert(self, data : int):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" -> ".join(result))


def addTwoLinkedListAndPrint(ptr1, ptr2):
    carry = 0
    while ptr1 is not None or ptr2 is not None or carry > 0:
        sumValue = carry
        if ptr1 is not None:
            sumValue += ptr1.data
            ptr1 = ptr1.next
        if ptr2 is not None:
            sumValue += ptr2.data
            ptr2 = ptr2.next
        print(sumValue % 10)
        carry = sumValue // 10


ll1 = Linkedlist()
ll1.insert(1)
ll1.insert(1)

ll2 = Linkedlist()
ll2.insert(0)
ll2.insert(9)
ll2.insert(9)

# Add them together (in-place mutating ll1)
ll1.head = addTwoLinkedListAndPrint(ll1.head, ll2.head)
