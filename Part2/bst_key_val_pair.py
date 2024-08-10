
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
#print(tree.key)
#print(tree.value)
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

#print(list_all(tree))

"""BALANCED BINARY TREES
difference between ledt sub tree and right sub tree is not more than 1
"""

#write a finction to determine if a binaru tree is balanced
def is_balanced(node):
    """Method that checks if a bst is balanced"""
    if node is None:
        return True, 0
    
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)

    balanced = balanced_l and balanced_r and abs(height_l- height_r) <= 1
    height = max(height_r, height_l) + 1

    return balanced, height


balanced, height = is_balanced(tree)
print(balanced)
print(height)


"""Write a function that creates a balanced binary search tree from a sorted list of key-val pairs"""
def make_balanced_bst(data, lo=0,hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]
    print(f"Value of key: {key} and value:{value}")

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root

data = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]

tree = make_balanced_bst(data)

#print(tree.key)
#print(tree.left.value)

"""Write a fuction that can balance a unbalanced tree"""
def balanced_bst(node):
    return make_balanced_bst(list_all(node))


