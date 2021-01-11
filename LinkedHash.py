class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        if not self.head:
            newNode = Node(data)
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    #using i to keep track of the tempKey's position in the list. As a result, can add temp 1 index behind tempKey.

    def remove(self, key):
        i = 0
        tempKey = self.head
        temp = None
        while i <= self.length - 1:
            if tempKey is None:
                return -1
            if i == 1:
                temp = self.head
            if i == 0 and tempKey.data[0] == key:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                return
            elif tempKey.data[0] == key:
                temp.next = temp.next.next
                self.length -= 1
                if temp.next is None:
                    self.tail = temp
                return
            if i >= 1:
                tempKey = tempKey.next
                temp = temp.next
                i += 1
            else:
                tempKey = tempKey.next
                i += 1
        return -1

    def search(self, key):
        i = 0
        temp = self.head
        while i <= self.length:
            if temp is None:
                return -1
            if temp.data[0] == key:
                return temp.data
            temp = temp.next
            i += 1
        return -1

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size

    def __str__(self):
        return f"size: {self.size}\narray: {self.arr}"

    def hash1(self, key):
        return len(key) % self.size

    def insert(self, key, value):
        index = self.hash1(key)
        if not self.arr[index]:
            link = LinkedList()
            link.append([key, value])
            self.arr[index] = link
        else:
            self.arr[index].append([key, value])

    def removeArr(self, key):
        index = self.hash1(key)
        if self.arr[index]:
            return self.arr[index].remove(key)
        return -1

    def searchArr(self, key):
        index = self.hash1(key)
        if self.arr[index]:
            return self.arr[index].search(key)
        return -1

    def print(self):
        for i in range(self.size):
            if self.arr[i]:
                self.arr[i].print_list()
                print()
            else:
                print('None')

h = ChainedHashTable(6)
h.insert('hash', 100)
h.insert('keqing', 42)
h.insert('kaeya', 5823)
h.insert('lisa', 421)
h.insert('childe', 12525)
h.insert('zhongli', 14)
h.insert('amber', 1)
h.insert('klee', 2553)
h.removeArr('zhongli')
h.removeArr('klee')
h.insert('awfsgsf', 242)
print(h.removeArr('gag'))
print(h.searchArr('hash'))
print(h.searchArr('lisa'))
print(h.searchArr('hello'))





h.print()







