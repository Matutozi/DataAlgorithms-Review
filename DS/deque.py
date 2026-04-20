class Node:
    def __init__(self, val):
        self.val = val
        self.next= None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    
    #Building the Operations
    def insertfront(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = self.rear = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def insertRear(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1

    def removeRear(self):
        if not self.rear:
            return None

        val = self.rear.val

        if self.head == self.rear:
            self.head = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return val


    def removeFront(self):
        if not self.head:
            return None
        
        val = self.head.val

        if self.head == self.rear:
            self.head = self.rear = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return val