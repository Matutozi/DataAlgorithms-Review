"""Write a code that implements the zippper method,
alternating between two linked list while always starting from the first list and alternating between the two lists
"""

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


def zipper_lists(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0


    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2

    return head1.value

print(zipper_lists(a, c))

#RECURSIVE APPROACH

def recursive_zipper_list(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head2 is None:
        return head1
    if head1 is None:
        return head2
    next1 = head1.next
    next2 = head2.next

    head1.next = head2
    head2.next = recursive_zipper_list(next1, next2)
    return head1

