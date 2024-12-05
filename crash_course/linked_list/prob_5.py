"""Code that reverses a linked list"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

""""Code that reverses the linked list and returns the head of the new linked list"""

def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.value

print(reverse_list(a))


#recursove approach
def recursive_reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    recursive_reverse_list(next, head)
    
