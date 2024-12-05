"""Code to find an value in a linked list"""


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


def find_element(head, target):
    """method that finds a value from a linked list"""
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next

    return False

print(find_element(a, 3))


"USING RECURSION APPROACH"

def recursive_find(head, target):
    if head is None:
        return False
    if head.value == target:
        return True
    return recursive_find(head.next, target)

print(recursive_find(a, 3))