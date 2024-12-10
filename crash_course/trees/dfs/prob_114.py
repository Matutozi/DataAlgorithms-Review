"""Flatten binary tree to linked list
Given the root of binary tree, flatten the tree into a linked list

"""

def flatten(root):
    """given the root of a binary tree return the linked list represenation of the tree
    Solving it recursively 
    time- O(n)
    space - O(h)
    """
    #to flatteen the root tree and return the list tail
    def dfs(root):
        if not root:
            return None
        left = dfs(root.left)
        right = dfs(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        last = right or left  or root
        return last
    dfs(root)

