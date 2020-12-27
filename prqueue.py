# Priority Queue using Binary Heap - Max

class Node():

    def __init__(self, prior):
        #self.index = 1
        self.priority = prior
        #self.left = None
        #self.right = None
        #self.parent = None

    def getData(self):
        return self.priority

class Heap():

    def __init__(self, size):
        self.size = size
        self.currSize = 0
        self.list = [None]*size
        #self.root = None

    def insert(self, value):
        if self.currSize == 0:
            self.list[1] = Node(value)
            self.currSize += 1
        else:
            self.list[self.currSize + 1] = Node(value)
            self.currSize += 1
            self.heapUp(value, self.currSize)

    def heapUp(self, val, current):
        parent = int(current / 2)
        if val > self.list[parent].getData(): #value being added is greater than parent
            temp = self.list[current]
            self.list[current] = self.list[parent]
            self.list[parent] = temp
            if parent > 1:
                self.heapUp(val, parent)

    def removeMax(self):
        self.list[1] = self.list[self.currSize]
        self.list[self.currSize] = None
        self.currSize -= 1
        value = self.list[1].getData()
        index = 1
        if self.currSize > 1:
            self.heapDown(index)
        #print(self.list[1].getData())

    def heapDown(self, ind):
        if self.list[ind].getData() < self.list[2*ind].getData():
            if self.list[2*ind].getData() < self.list[2*ind + 1].getData():
                temp = self.list[ind]
                self.list[ind] = self.list[2*ind + 1]
                self.list[2*ind + 1] = temp
                ind = 2*ind + 1
                if (ind*2 + 1) <= self.currSize:
                    self.heapDown(ind)
            else:
                temp = self.list[ind]
                self.list[ind] = self.list[2*ind]
                self.list[2*ind] = temp
                ind = 2*ind
                if (ind*2 + 1) <= self.currSize:
                    self.heapDown(ind)
        else:
            if self.list[2*ind + 1] and (self.list[ind] < self.list[2*ind + 1]):
                temp = self.list[ind]
                self.list[ind] = self.list[2*ind + 1]
                self.list[2*ind + 1] = temp
                ind = 2*ind + 1
                if (ind*2 + 1) <= self.currSize:
                    self.heapDown(ind)


    def print(self):
        newList = []
        for i in range(1, self.currSize+1):
            if self.list[i] is not None:
                newList.append(self.list[i].getData())
        print(newList)


if __name__=="__main__":
    x = Heap(10)
    x.insert(100)
    x.insert(80)
    x.insert(120)
    x.insert(90)
    x.insert(110)
    x.insert(50)
    x.insert(200)
    x.print()
    x.removeMax()
    x.print()
    x.removeMax()
    x.print()
