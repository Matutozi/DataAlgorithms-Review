"""
To merge two list together
"""

"""
Time Complexity - O(m + n)
space complexity - O(1)
"""

class ListNode:
    """object that defines a class"""
    def __init__(self, value=0, nextNode=None):
        self.value = value
        self.next = nextNode

    def mergeTwoLists(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.value < l2.value:
            temp = head = ListNode(l1.value)
            l1 = l1.next
        else:
            temp = head = ListNode(l2.value)
            l2 = l2.next

        while l1 is not None and l2 is not None:
            if l1.value < l2.value:
                temp.next = ListNode(l1.value)
                l1= l1.next
            else:
                temp.next = ListNode(l2.value)
                l2 = l2.next
            
            temp = temp.next

        while l1 is not None:
            temp.next = ListNode(l1.value)
            l1 = l1.next
            temp  = temp.next

        while l2 is not None:
            temp.next = ListNode(l2.value)
            l2= l2.next
            temp = temp.next

        return head

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_list = ListNode().mergeTwoLists(l1, l2)
    print("Merged List:")
    while merged_list is not None:
        print(merged_list.value, end=" ")
        merged_list = merged_list.next
