"""
Average of levels in binary tree
given the root of binary tree, return the average value of node on each level in the form of an array

"""
import collections
def list_average(root):
    """Method that returns the average of each level of binary tree and store values in an array"""

    result = list()
    tmp_queue = collections.deque()

    if not root:
        return result
    
    tmp_queue.append(root)

    while tmp_queue:
        length = len(tmp_queue)
        level = []

        for i in range(length):
            node = tmp_queue.popleft()
            if node:
                level.append(node.value)
                tmp_queue.append(node.left)
                tmp_queue.append(node.right)
        if level:
            average = sum(level) / len(level)
            result.append(average)
    return result