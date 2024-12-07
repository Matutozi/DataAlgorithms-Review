"""
Maximum depth of binary tree
given the root of a binary tree, return its maximum depth

"""
import collections
def maxDepth(root):
    """Method that returns the depth of a binary tree"""
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def another(root):
    """Using bfs
    level order traversal
    """
    if not root: return 0
    level = 1
    queue = collections.deque([root])
    while queue:
        lent = len(queue)
        for i in range(lent):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.appenf(node.right)
        level += 1
    
    return level

def iterative_dfs(root):
    pass


