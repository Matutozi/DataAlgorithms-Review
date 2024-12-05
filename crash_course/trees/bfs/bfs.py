"""Calculate the height of the tree
start from the root node
stire children of node in array
first in first out (QUEUE)
time complexity - O(n)
space complexity -  
Question - leetcode 102 (binary tree level order traversal)
returns a list of list containing the 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
def list_order_traversal(root):
    """
    Given the root of binary tree, return the level order traversal of its node values from
    left to right
    """
    result = list()

    q = collections.deque()
    q.append(root)

    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level.append(node.value)
                q.append(node.left)
                q.append(node.right)
        if level:
            result.append(level)

    return result