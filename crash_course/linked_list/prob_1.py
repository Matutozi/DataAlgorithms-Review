"""given a lknked list head node, return an array containing all the values of the linked list"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next = b
b.next = c
c.next = d
d.next = e

def linked_list_values(head):
    values = list()
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next

    return values


print(linked_list_values(a))


"""TO implemtent recursecely"""

def linked_lst_val_rec(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head is None:
        return
    values.append(head.value)
    fill_values(head.next, values)


print(linked_lst_val_rec(a))