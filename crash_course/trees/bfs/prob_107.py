"""Binary tree order traverasl II
given the root of a  binary tree, return the bottom up level order traversal of its node values
from left to right level , level by level from leaf to root
"""
import collections
def levelOrderBottom(root):
    """Method that traverses a binary tree and returns the bottom to top traversal"""
    result = list()

    queue = collections.deque()
    queue.append(root)
    if root is None:
        return result
    
    while queue:
        lent = len(queue)
        layer = []

        for i in range(lent):
            node = queue.popleft()
            if node:
                layer.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        result.insert(0, layer)
    
    return result
