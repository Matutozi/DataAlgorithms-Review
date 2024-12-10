"""GIven the root of a binary search tree, and an interger, return the smallest value"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Using inorder traversal [L N R]"""
        self.count = 0  # Initialize the count once

        def inorder(node):
            if not node:
                return None

            # Traverse left subtree
            result = inorder(node.left)
            if result is not None:
                return result

            # Process current node
            self.count += 1
            if self.count == k:
                return node.val

            # Traverse right subtree
            return inorder(node.right)

        return inorder(root)
