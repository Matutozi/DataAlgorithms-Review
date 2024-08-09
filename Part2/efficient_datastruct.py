"""A more efficient solution to the darastruct database is implemented by using binary trees
root, leaves, nodes

it must be balanced on both sides"""

#INPLEMENTATION OF BINARY TREE
#they are used in file system to locate a file
"""Implemt a binary tree in python and show its usage"""


class TreeNode:
    """MEthod that implements the tree node syestm"""
    def __init__(self, key, left=None, right= None):
        self.key = key
        self.left = left
        self.right = right

node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(4)

node0.left = node1
node0.right = node2
#print(node0)
tree = node0

ans = tree.key
#print(ans)
#print(tree.left.key)
#print(tree.right.key) 

"""We can use a helper function that helps with the construction of the tree"""
#tuple(left sub tree, key, right subtree)

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7,8)))

def parse_tuple(data):
    """METHOD THAT CONVERTS A tuple into tree like format"""
    #print(data)
    #check if data is of type tuple
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        #use recursion
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

    elif data is None:
        node = None
    else:
        node = TreeNode(data)

    return node


tree2 = parse_tuple(tree_tuple)
print(tree2)
print(tree2.right.right.right.key)

#TRY TO DEFINE A FUNCTION THAT CONVERTS A TREE TO A TUPLE


"""TRAVERSING A BINARY TREE
moving through an element of a binary tree once
- inorder LMR
- preorder
- post order
"""

#INORDER TRAVERSAL
def traverse_in_order(node):
    """METHOD THAT IMPLEMENTS TRAVERSAL IN ORDER"""
    if node is None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

print(traverse_in_order(tree2))