"""
Binary trees zigzag level order traversal
Given the root of a binary tree, return the zig zag level order traversal of its node values, 
LEFT to RIGHT , then RIGHT to LEFT for next level and alternate 
"""

import collections

def zigzaglevelorder(root):
    """Method that implements the zig zagging of a binary tree
    normal order-> remove from front add at back
    reverse order -> the approach would be to add the new levels to the front of the previous levels and remove
    from the end"""
    result = list()
    tmp_queue = collections.deque()
    
    if root:
        tmp_queue.append(root)
    else:
        return result
    
    while tmp_queue:
        length = len(tmp_queue)
        level = list()

        for i in range(length):
            node = tmp_queue.popleft()
            if node:
                level.append(node.val)
                tmp_queue.append(node.left)
                tmp_queue.append(node.right)
        
        if len(result) % 2:
            level.reverse()
        if level:
            result.append(level)

    return result