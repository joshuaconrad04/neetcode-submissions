class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):

        self.head = ListNode(0)
        self.rear = self.head
        self.max_size = k
        self.size = 0
        
    def enQueue(self, value: int) -> bool:

        #full queue
        if self.size==self.max_size:
            return False

        #empty queue
        if not self.head.next:
            self.head.next = ListNode(value)
            self.rear = self.head.next
            self.rear.next = self.head
            self.size+=1
        #non empty queue
        else:
            new_node = ListNode(value)
            self.rear.next = new_node
            self.rear = self.rear.next
            self.rear.next = self.head
            self.size+=1
        return True

    def deQueue(self) -> bool:

        #if queue is empty
        if not self.head.next or self.size==0:
            return False
        self.head.next = self.head.next.next
        self.size -= 1

        if self.size == 0:
            self.rear = self.head

        return True

    def Front(self) -> int:
        if not self.head.next or self.size==0:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if not self.head.next or self.size==0:
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        if not self.head.next or self.size==0:
            return True
        return False

    
    def isFull(self) -> bool:
        return self.size == self.max_size

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()