class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()