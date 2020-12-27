#Hash Table
"""insert - adds a K:V pair to the hashtable
get - returns a value, given a key
getKeys - returns all keys within a list
getVals - returns all values within a list
remove - removes a K:V pair from hashTable
hash - converts a key to an index via hashing
search - returns true if K:V pair found, -1 otherwise
isEmpty - returns true if hashTable is empty
capacity - returns the size of the hashTable
clear - resets the hashTable
resize - increases size and rehashes all elements"""

class HashTable:

    def __init__(self, size):
        self.list = [None]*size
        self.currSize = 0
        self.totalSize = size

    def insert(self, key, val):
        if self.currSize == self.totalSize:
            self.resize()

        index = self.hash(key)

        #handle collision, linear probing, and arriving at end
        while self.list[index]:
            if index != self.totalSize - 1:
                index += 1
            else:
                index = 0

        self.list[index] = (key, val)
        self.currSize += 1

    def hash(self, key):
        num = 1
        for k in key:
            num += ord(k)

        num =  num % (self.totalSize-1)
        return num

    def resize(self):
        temp = self.list
        self.totalSize *= 2
        newHashT = HashTable(self.totalSize)

        for i in temp:
            newHashT.insert(i[0], i[1])

        self.list = newHashT.list
        return newHashT

    def getKeys(self):
        keyList = []
        [keyList.append(tu[0]) for tu in self.list if tu]
        return keyList

    def getVals(self):
        valList = []
        [valList.append(tu[1]) for tu in self.list if tu]
        return valList

    def getVal(self, key):
        listKeys = []
        count = 0
        i = self.hash(key)

        if self.list[i] == None:
            return listKeys
        else:
            while self.list[i] is not None:
                if self.list[i][0] == key:
                    listKeys.append(self.list[i][1])
                    count += 1
                if count == self.totalSize - 1:
                    return listKeys
                if i != self.totalSize - 1:
                    i += 1
                else:
                    i = 0
        return listKeys

    def remove(self, key, val):
        i = self.hash(key)
        while self.list[i] and self.list[i][1] != val:
            i += 1
        self.list.pop(i)
        return

if __name__ == "__main__":

    x = HashTable(5)
    x.insert("haseeb", 101456)
    x.insert("zain", 523424)
    x.insert("john", 78576353)
    x.insert("maheen", 686576)
    x.insert("aleem", 222)
    x.insert("william", 12684)
    x.insert("Ari", 17122684)
    x.insert("Elly", 1111)
    x.insert("sohaila", 35353)
    x.insert("javed", 245)
    x.insert("tono", 888)
    x.insert("haseeb", 999)
    print(x.list)
    print(x.getKeys())
    print(x.getVals())
    print(x.getVal("haseeb"))
    print(x.getVal("aaa"))
    print(x.remove("haseeb", 999))
    print(x.remove("aleem", 222))
    print(x.list)
