#Binary Search Tree

from queue import Queue

class Node:

    def __init__(self, value): # constructor
        self.data = value
        self.left = None
        self.right = None

    def getData(self):
        return self.data


class BST:

    def __init__(self): # constructor
        self.root = None
        self.height = -1

    def getRoot(self):
        return self.root

    def insert(self, subroot, val):

        if self.root is None: #an empty BST
            self.root = Node(val)
            self.height += 1
        else:
            if val < subroot.data:
                if subroot.left == None:
                    subroot.left = Node(val)
                    if subroot.right is None:
                        self.height += 1

                else:
                    self.insert(subroot.left, val)
            else:
                if subroot.right == None:
                    subroot.right = Node(val)
                    if subroot.left is None:
                        self.height += 1
                else:
                    self.insert(subroot.right, val)

    def treeHeight(self, subroot):

        if subroot is None:
            return -1
        else:
            return 1 + max(self.treeHeight(subroot.left), self.treeHeight(subroot.right))

    def inOrder(self, subroot): # print inOrder

        list = []
        self.__inOrderHelper(list, subroot)
        return list

    def __inOrderHelper(self, list, subroot):

        if subroot is None:
            return
        else:
            self.__inOrderHelper(list, subroot.left)
            list.append(subroot.getData())
            self.__inOrderHelper(list, subroot.right)

    def postOrder(self, subroot): # print inOrder

        list = []
        self.__postOrderHelper(list, subroot)
        return list

    def __postOrderHelper(self, list, subroot):

        if subroot is None:
            return
        else:
            self.__postOrderHelper(list, subroot.left)
            self.__postOrderHelper(list, subroot.right)
            list.append(subroot.getData())

    def preOrder(self, subroot): # print inOrder

        list = []
        self.__preOrderHelper(list, subroot)
        return list

    def __preOrderHelper(self, list, subroot):

        if subroot is None:
            return
        else:
            list.append(subroot.getData())
            self.__preOrderHelper(list, subroot.left)
            self.__preOrderHelper(list, subroot.right)

    def bstPrint(self, subroot):

        self.__printHelper(subroot, 0)
        return

    def __printHelper(self, subroot, i):
        if subroot is None:
            return
        else:
            i += 1
            self.__printHelper(subroot.right, i)
            print(i*"    ", subroot.getData())
            self.__printHelper(subroot.left, i)

    def minimum(self, subroot):
        temp = subroot
        while temp.left:
            temp = temp.left

        return temp

    def maximum(self, subroot):
        temp = subroot
        while temp.right:
            temp = temp.right

        return temp.getData()

    def search(self, subroot, val):

        if subroot is None:
            #print("Not Found")
            return False
        else:
            if subroot.getData() is not val:
                if val < subroot.getData():
                    return self.search(subroot.left, val)

                else:
                    return self.search(subroot.right, val)
            else:
                #print("Found")
                return True

    def levelT(self, subroot):

        list = []
        q = Queue()
        q.enqueue(subroot)

        while not q.isEmpty():

            a = q.dequeue()

            if a.left is not None:
                q.enqueue(a.left)

            if a.right is not None:
                q.enqueue(a.right)

            list.append(a.getData())

        return list


    def remove(self, subroot, val):
        parent = None
        isRight = False
        current = subroot

        while current.getData() != val:

            if val < current.getData():
                isRight = False
                parent = current
                current = current.left

            else:
                isRight = True
                parent = current
                current = current.right

        # Node being removed has no children
        if current.right is None and current.left is None:
            if isRight == True:
                parent.right = None
            else:
                parent.left = None
            del current
            return

        #Node being removed has one child
        if current.right is None or current.left is None:

            if isRight == False: #if node is a left child itself
                if current.right is None: #Node being removed has left child
                    parent.left = current.left
                    del current
                    return
                else: #node being removed has right child
                    parent.left = current.right
                    del current
                    return

            else: #if node is a right child itself
                if current.right is None: #node being removed has left child
                    parent.right = current.left
                    del current
                    return
                else: #node being removed has right child
                    parent.right = current.right
                    del current
                    return

        # Node being removed has two or more children
        # Right child will replace node being removed
        if current.right and current.left:

            temp_m = self.minimum(current.right)
            self.remove(current.right, temp_m.getData())
            current.data = temp_m.data

            """if temp_r.left is None: #if right child has no left child
                current = current.right #make the right child the new current
                current.left = temp_l #assign new current the old left child
                if isRight is False: #if node being removed a left child
                    parent.left = current # make the new node the parent's new left
                    return
                else:
                    parent.right = current
                    return

            #if right child has left children, find the smallest one and
            #make it the new parent of the deleted node's left children
            else:
                temp_m = self.minimum(temp_r.left)
                current = current.right
                temp_m.left = temp_l
                if isRight is False:
                    parent.left = current
                    return
                else:
                    parent.right = current
                    return"""

if __name__ == "__main__":
    x = BST()
    y = x.getRoot()
    x.insert(y, 5)
    y = x.getRoot()
    x.insert(y, 6)
    x.insert(y, 3)
    x.insert(y, 4)
    x.insert(y, 1)
    x.insert(y, 2)
    #x.insert(y, 4)
    x.insert(y, 8)
    x.insert(y, 15)
    x.insert(y, 17)
    x.insert(y, 12)
    x.insert(y, 10)
    x.insert(y, 11)
    x.insert(y, 25)
    x.insert(y, 20)
    x.insert(y, 18)
    x.insert(y, 16)


    x.insert(y, 0)
    print("InOrder is : ", x.inOrder(y))
    print("PreOrder is: ", x.preOrder(y))
    print("PostOrder is: ", x.postOrder(y))
    print(x.treeHeight(y))
    print(x.minimum(y).getData())
    print(x.maximum(y))
    print(x.search(y, 6))
    print(x.levelT(y))
    x.remove(y, 15)
    print(x.levelT(y))
    print("InOrder is : ", x.inOrder(y))
    print(x.treeHeight(y))
    x.bstPrint(y)
