# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ

from typing import Optional
import collections
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        """to find if x and y are cousins, if they are cousins they would have same depth but different parents"""
        if not root:
            return False

        if root is not None:
            t_queue = collections.deque([(root, None)]) #to store the node, parent
        
        while t_queue:
            size = len(t_queue)

            x_parent=None
            y_parent = None

            for i in range(size):
                node, parent = t_queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    t_queue.append((node.left, node))
                if node.right:
                    t_queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent
            
            if x_parent or y_parent:
                return False
        return False





