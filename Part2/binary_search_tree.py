"""
Write a code to check if a binary tree is a binary search tree
write a function to find the maximum key in a binary tree
write a function to find the minimum key in a binary tree
"""

class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_binary_search_tree(node):
    """MEthod that implements the three questions above in one"""
    if node is None:
        return True, None, None
    is_bst_l,  min_l, max_l = is_binary_search_tree(node.left)
    is_bst_r, min_r, max_r = is_binary_search_tree(node.right)

    is_bst_node = (is_bst_l and is_bst_r) and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r)

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))


    return is_bst_node, min_key, max_key


root = (10, (5, None, None), (15, None, None))

is_bst, min_key, max_key = is_binary_search_tree(root)
