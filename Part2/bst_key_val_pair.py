
"""Script that implements class that stores user object with each key in bst"""

from datastruct import jadhesh, biraj, siddhant, sonaksh, vishal

class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  #point to parent node

tree = BSTNode(jadhesh.username, jadhesh)

#print(tree.key)
#print(tree.value)

tree.left = BSTNode(biraj.username, biraj)
tree.left.parent = tree
tree.right = BSTNode(sonaksh.username, sonaksh)
tree.right.parent = tree

#print(tree.left.key)
#print(tree.right.key)


"""Write a method that inserts a node into a binary search tree"""
def insert(node, key, value):
    """Method that inserts a node at any location in a bst"""
    if node is None:
        node = BSTNode(key, value)
    
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, jadhesh.username, jadhesh)
print(tree.key)
print(tree.value)
insert(tree, biraj.username, biraj)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, vishal)

#note the norder in ehich nodes are inserted can cause balances or unbalanced 

"""Method that finds a value in a given bst"""
def find(node, key):
    """Method to find a value """
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return (find(node.right, key))
    
"""Method that updates a value in a given bst"""
def update(node, key, value):
    if node is None:
        return None
    target = find(node, key)
    if target is not None:
        target.value = value
    
"""method that lists all the nodes"""
def list_all(node):
    if node is None:
        return []
    return (list_all(node.left) + [node.value] + list_all(node.right))

print(list_all(tree))

