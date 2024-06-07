from singleLinkedList import (
    SingleLinkedList,
)

def main():
    singlell = SingleLinkedList()
    import random
    L = range(100)
    amount = 7
    inputArr = [random.choice(L) for _ in range(amount)]
    for val in inputArr:
    	singlell.insertEnd(val)
    singlell.displayLinkedList()
    dataDel = inputArr[random.choice(range(1, 7))]
    singlell.deleteNode(dataDel)
    singlell.deleteNode(-10) # outside of range(100)
    print()
    singlell.displayLinkedList()


if __name__ == "__main__":
    main()