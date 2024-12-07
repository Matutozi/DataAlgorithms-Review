"""Convert sorted array to binary search tree

given an integer array nums where elements are sorted in ascending order, 
convert it to a height balanced binary search tree

"""

def sortedArrayBST(nums):
    mid = len(nums)  / 2

    if not nums:
        return None
    
    root = TreeNode(val=nums[mid])
    root.left = sortedArrayBST(nums[:mid])
    root.right = sortedArrayBST(nums[mid+1:])

    return root
    