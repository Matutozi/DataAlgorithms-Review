"""Populating next right pointer in each node
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children
"""

import collections
#traverse using bfs, using queue
def connect(root):
    """traverse every node"""

    result = list()

    queue = collections.deque()

    if root:
        queue.append(root)

    while queue:
        lent = len(queue)
        prev = None
        layer = []

        for i in range(lent):
            node = queue.popleft()
            if prev:
                prev.next = node
            prev = node
        
            if node:
                queue.append(node.left)
                queue.append(node.right)
    return root
      