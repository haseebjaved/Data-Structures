  # Stack
  # Goals:																						Desired Runtime
  # push -> add an element to the stack											O(1)
  # pop -> remove and return element from the stack					O(1)
  # peek -> return the top item															O(1)
  # is_empty -> return true if empty 												O(1)


class Stack:
    # Constructor
    def __init__(self):
        self.list = []
        self.top = -1
        pass

    def push(self, x):
        self.list.append(x)
        self.top += 1
        print(self.list)

    def pop(self):
        if self.top >= 0:
            p = self.list.pop(self.top)
            self.top -= 1
            print(self.list)
            return p

    def peek(self):
        print(self.list[self.top])
        return self.list[self.top]

    def is_empty(self):
        print(self.top == -1)

    def printStack(self):
        print(self.list)


if __name__ == "__main__":
    y = Stack()
    y.push(5)
    y.push(10)
    y.pop()
    y.is_empty()
    y.printStack()
    peek_val = y.peek()

    print(y.pop())
