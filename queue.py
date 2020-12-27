from LinLis import LinkedList

class Queue():

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, val):
        self.queue.add(val, self.queue.getLength())

    def dequeue(self):
        return self.queue.remove(0)

    def peek(self):
        return self.queue.peek()

    def isEmpty(self):
        return self.queue.getLength() == 0

    def print(self):
        print(self.queue.print())

if __name__ == "__main__":

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.print()

    while q.isEmpty() is False:
        print(q.dequeue())
        q.print()

    """q = Queue()
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(8)
    q.enqueue(1)
    q.enqueue(13)
    q.print()
    print(" the first item is: ", q.peek())
    print("is the queue empty: ", q.isEmpty())
    q.dequeue()
    q.print()
    q.dequeue()
    q.print()"""
