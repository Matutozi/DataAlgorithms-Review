"""TO IMPLEMENT BINARY TREE

Each Node has at most 2 children
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insertRoot(self, val):
        self.root = TreeNode(val)

    def attach(self, parent, left=None ,right=None):
        if left is not None:
            parent.left = TreeNode(left)
        
        if right is not None:
            parent.right = TreeNode(right)
        
    
    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def preOrder(self, node):
        if not node:
            return
        
        self.preOrder(node.root)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if not node:
            return
        
        self.postOrder(node.left)
        self.postOrder(node.right)
        self.postOrder(node.root)
    