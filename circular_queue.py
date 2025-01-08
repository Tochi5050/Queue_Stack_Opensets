class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k #creating a static array
        self.count = 0
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        self.queue[(self.head + self.count) % self.size] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        self.tailIndex = (self.head + self.count - 1) % self.size
        return self.queue[self.tailIndex]

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