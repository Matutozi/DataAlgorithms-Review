"""Symmetric tree
GIven the root of  binary tree, check whether it is a mirror of itself
symmetric around its center

"""
import collections
from typing import Optional, List

def isSymmetric(root):
    """Method to find if a tree is symmetric"""
    if not root:
        return True

    queue = collections.deque([root.left, root.right])

    while queue:
        left, right = queue.popleft(), queue.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False
        
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True