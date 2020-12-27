#Linked List

class Node:
  # Constructor
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

class LinkedList:
# Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, val, index):
        i = 0 #add to the front and make it head
        if index == 0:
            if self.head == None:
                new_node = Node(val)
                self.head = new_node
                self.tail = new_node
                self.length += 1

            else:
                temp = self.head
                new_node = Node(val)
                new_node.next = temp
                self.head = new_node
                self.length += 1

        elif index == self.length: #add and make it tail
            temp = self.tail
            new_node = Node(val)
            self.tail = new_node
            temp.next = self.tail
            self.length += 1

        else: #add to after head and before tail
            temp = self.head
            temp_prev = None
            while i != index:
                temp_prev = temp
                temp = temp.next
                i += 1

            new_node = Node(val)
            new_node.next = temp
            temp_prev.next = new_node
            self.length += 1

    def remove(self, index):
        i = 0

        if index == None:
            return

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.getData()

        if index == 0: # remove first item
            temp = self.head
            self.head = temp.next
            self.length -= 1
            return temp.getData()


        elif (index > 0) and (index < self.length - 1):
            #removing item in middle
            temp = self.head
            temp_prev = None
            while i != index:
                temp_prev = temp
                temp = temp.next
                i += 1

            temp_prev.next = temp.next
            self.length -= 1

        else:
            #removing last item
            temp = self.head
            temp_prev = None
            while i != index:
                temp_prev = temp
                temp = temp.next
                i += 1

            self.tail = temp_prev
            temp_prev.next = None
            self.length -= 1

    def print(self): # print the LinkedList
        temp = self.head
        ll_str = ""
        while temp is not None:
            ll_str += str(temp.getData()) + " -> "
            temp = temp.next

        return ll_str

    def peek(self):
        return self.head.getData()

    def getLength(self):
        return self.length

    """def search(self, va):
        temporary = self.head
        ind = 0
        while temporary is not None:
            if temporary.getData() == va:
                return ind
            else:
                temporary = temporary.next
                ind += 1
        return"""

    def search(self, va):
        temporary = self.head
        ind = 0
        while temporary.getData() != va:
            temporary = temporary.next
            ind += 1
        return ind

if __name__ == "__main__":
    """y = [1, 2, 4, 5]
    x = LinkedList(y)
    print(x.print())"""
    x = LinkedList()
    x.add(1000, 0)
    x.add(99, 1)
    x.add(33, 2)
    x.add(45, 2)
    x.add(56, 4)
    print(x.print())
    print(x.search(33))
    x.remove(1)
    print(x.print())
    x.remove(0)
    print(x.print())
    x.remove(0)
    print(x.print())


    """w = LinkedList(Node(5))
    print(w.print())"""
