"""Code that takes an index and returns the corresponding values from linked list"""

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


def get_node_value(head, index):
    """Method that retuns a value in a linked list given the index/position"""
    current = head
    if current is None:
        return None
    
    if index == 0:
        return current.value
    
    return get_node_value(current.next, index - 1)

print(get_node_value(a, 2))



def recursive_find(head, index):
    current = head
    count = 0
    while current is not None:
        if count == index:
            return current.value
        count += 1
        current = current.next

    return None

print(recursive_find(a, 3))