"""
Binary Tree Right Side View

Definition for a binary tree node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Method that returns only the right children from a tree"""
        result = list()
        temp_queue = collections.deque()
        temp_queue.append(root)

        while temp_queue:
            lent = len(temp_queue)
            #level = []

            for i in range(lent):
                node = temp_queue.popleft()
                

                if node:
                    if i == lent - 1:
                        result.append(node.val)
                    if node.left:
                        temp_queue.append(node.left)
                    if node.right:
                        temp_queue.append(node.right)
                    
        return result
        