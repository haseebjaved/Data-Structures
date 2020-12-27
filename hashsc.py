"""A hashTable of fixed-size that resolves collision handling through separate chaining.
Assumes the K:V pair is inputted as a tuple:
    put - adds a K:V pair to the hashtable
    get - returns value with same key
    getKeys - returns all keys from hashTable
    getVals - returns all values from hashTable
    remove - removes a K:V pair from hashTable
    hash - converts a key to an index via hashing
    isEmpty - returns true if hashTable is empty
    getCapacity - returns the size of the hashTable
    clear - resets the hashTable
    resize - resizes the hashTable, according to newsize
    print - prints the hashTable"""

from LinLis import LinkedList

class HashSC():

    def __init__(self, size):
        self.totalSize = size
        self.list = [None]*size
        self.currSize = 0

    def put(self, key, val):
        if self.currSize > self.totalSize*3:
            self.resize(self.currSize*2)

        i = self.hash(key)

        if self.list[i] == None:
            self.list[i] = LinkedList()
            self.list[i].add((key, val), 0)
            self.currSize += 1
            return False

        else:
            self.list[i].add((key, val), self.list[i].getLength())
            self.currSize += 1
            return

    def hash(self, key):
        num = 1
        for k in key:
            num += ord(k)

        num =  num % (self.totalSize-1)
        return num

    def get(self, key):
        i = self.hash(key)
        result = []
        if self.list[i] is None: # Empty index, None value
            return False
        else:
            temp = self.list[i].head #Begin iterating the LinkedList at Head
            while temp: #While not the end of the LinkedList
                a = temp.getData()
                if a[0] == key:
                    result.append(a[1]) #append to a list if multiple keys
                temp = temp.next
        return result

    def rem(self, key, val):
        i = self.hash(key)
        if self.list[i] == None:
            return
        else:
            temp = self.list[i]
            x = temp.search((key, val))
            self.list[i].remove(x)

    def hprint(self):
        for i in range(self.totalSize):
            if self.list[i] == None:
                print(i)
            else:
                x = self.list[i]
                print(i, ":", x.print())

    def resize(self, newsize):
        temp = self.list
        newHashT = HashSC(newsize)

        for ll in temp:
            if ll is not None:
                t = ll.head
                while t is not None:
                    k, v = t.getData()
                    newHashT.put(k, v)
                    t = t.next
        self.list = newHashT.list
        self.totalSize = newHashT.totalSize
        self.currSize = newHashT.currSize

if __name__ == "__main__":

    x = HashSC(5)
    x.put("haseeb", 101456)
    x.put("zain", 523424)
    x.put("john", 78576353)
    x.put("maheen", 686576)
    x.put("aleem", 222)
    x.put("william", 12684)
    x.put("Ari", 17122684)
    x.put("Elly", 1111)
    x.put("sohaila", 35353)
    x.put("sohaila", 1234)
    x.put("javed", 245)
    x.put("usman", 987)
    x.put("tono", 888)
    x.put("haseeb", 999)
    x.hprint()
    #print(x.get("Ari"))
    x.rem("john", 78576353)
    x.resize(40)
    x.hprint()
