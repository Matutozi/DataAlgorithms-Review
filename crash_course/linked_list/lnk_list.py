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


def print_list(head):
    #head is the first element of linked list
    current = head
    while current is not None:
        print(current.value)
        current = current.next

print_list(a)

def print_list_recursion(head):
    if head is None: 
        return
    
    print(head.value)
    #print(head.next)
    print_list_recursion(head.next)


print(print_list_recursion(a))