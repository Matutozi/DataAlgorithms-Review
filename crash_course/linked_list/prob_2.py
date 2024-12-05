"""Given a linked list return the sum of all the nodes"""

#traverse the linked list and add each iteration to a value

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

def linked_sum(head):
    current = head
    total_sum = 0
    while current is not None:
        total_sum += current.value
        current = current.next

    return total_sum

print(linked_sum(a))

#RECURSIVE APPROACJ

def linked_rec_sum(head):
    if head is None:
        return 0
    return head.value + linked_rec_sum(head.next)

print(linked_rec_sum(a))