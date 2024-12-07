"""
Invert Binary Tree
given the root of a binary tree, invert the tree and return its root
"""

def invertTree(root):
    """Method that inverst a binary tree
    time complexity - O(n)
    space- O(h) -> height of tree
    """
    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
    
    