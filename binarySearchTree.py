class stackNqueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

#stack using singly linked list
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, data):
        stack = stackNqueueNode(data)
        if not self.top:
            self.top = stack
            self.length += 1
            return
        stack.next = self.top
        self.top = stack
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        popped = self.top
        self.top = self.top.next
        popped.next = None
        self.length -= 1
        return popped

    def peek(self):
        if self.length == 0:
            return -1
        return self.top.data

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

#queue using singly linked list
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, data):
        node = stackNqueueNode(data)
        if not self.first and not self.last:
            self.first = node
            self.last = self.first
            self.length += 1
            return
        self.last.next = node
        self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return -1
        if self.length == 1:
            removed = self.last.data
            self.first = None
            self.last = None
            self.length -= 1
            return removed
        removed = self.first.data
        self.first = self.first.next
        removed.next = None
        self.length -= 1
        return removed

    def firstNlast(self):
        return f"first:{self.first} last:{self.last}"

#node for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        curr_node = self.root
        while True:
            if curr_node.data > data:
                if curr_node.left is None:
                    curr_node.left = node
                    return
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = node
                    return
                else:
                    curr_node = curr_node.right

    #removes a node from the tree by considering different cases
    def remove(self, data):
        #case of removing root
        if self.root == None:
            return 'Tree is Empty'
        elif self.root.data == data:
            if not self.root.right and not self.root.left:
                self.root = None
            elif not self.root.left and self.root.right:
                self.root = self.root.right
            elif not self.root.right and self.root.left:
                self.root = self.root.left
            else:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left
                if delNode.right:
                    #this would only happen if delNode had a left branch
                    if delNodeParent.data > delNode.right.data:
                        delNodeParent.left = delNode.right
                    #this would happen if del node didnt have a left branch
                    else:
                        delNodeParent.right = delNode.right
                    self.root.data = delNode.data
                    del delNode
            return True
        parent = None
        delNode = self.root
        while delNode.data != data and delNode:
            parent = delNode
            if delNode.data < data:
                delNode = delNode.right
            else:
                delNode = delNode.left
        #case: can't find value
        if delNode is None or delNode.data != data:
            return -1
        #case: node has no childen
        elif not delNode.right and not delNode.left:
            if parent.data > delNode.data:
                parent.left = None
            else:
                parent.right = None
        #case: node has only right child
        elif delNode.right and not delNode.left:
            if parent.data > delNode.data:
                parent.left = delNode.right
            else:
                parent.right = delNode.right
        #case node has only left child
        elif delNode.left and not delNode.right:
            if parent.data > delNode.data:
                parent.left = delNode.left
            else:
                parent.right = delNode.left
        #case: node has both children
        elif delNode.right and delNode.left:
            target = delNode
            parent = delNode
            delNode = delNode.right
            while delNode.left:
                parent = delNode
                delNode = delNode.left
            if delNode.right:
                if parent.data > delNode.data:
                    parent.left = delNode.right
                else:
                    parent.right = delNode.right
            else:
                if parent.data > delNode.data:
                    parent.left = None
                else:
                    parent.right = None
            target.data = delNode.data
            del delNode

    def printt(self):
        curr_node = self.root
        self.traverse(curr_node)


    def traverse(self, curr_node):
        if curr_node != None:
            self.traverse(curr_node.left)
            print(curr_node.data)
            self.traverse(curr_node.right)

    #care about printing parents first before children
    def Traverse_Preorder(self, root):
        curr = root
        if curr is None:
            return
        print(curr.data)
        self.Traverse_Preorder(curr.left)
        self.Traverse_Preorder(curr.right)

    def Traverse_Inorder(self, root):
        curr = root
        if curr is None:
            return
        self.Traverse_Inorder(curr.left)
        print(curr.data)
        self.Traverse_Inorder(curr.right)

    #care about printing children first then parents, hence post
    def Traverse_Postorder(self, root):
        curr = root
        if curr is None:
            return
        self.Traverse_Postorder(curr.left)
        self.Traverse_Postorder(curr.right)
        print(curr.data)

    def dfs_preorder(self):
        return self.Traverse_Preorder(self.root)

    def dfs_inorder(self):
        return self.Traverse_Inorder(self.root)

    def dfs_postorder(self):
        return self.Traverse_Postorder(self.root)

    #bfs using queue
    def BreadthFirstSearch(self):
        queue = Queue()
        queue.enqueue(self.root)
        while queue.length > 0:
            print(queue.first)
            curr = queue.dequeue()
            if curr.left:
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)





tree = BinarySearchTree()
tree.insert(20)
tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(60)
tree.insert(42)
tree.insert(55)
tree.insert(89)
tree.BreadthFirstSearch()

# dam = Stack()
# dam.push(10)
# print(dam.pop())
# print(dam.length)
# print(dam.peek())

# bam = Queue()
# bam.enqueue(10)
# bam.enqueue(23)
# bam.enqueue(42)
# bam.dequeue()
# print(bam.firstNlast())


