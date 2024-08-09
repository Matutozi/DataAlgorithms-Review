"""Given a rotated list, find the location of an element or value in the list using binary search with the complexity of log n
key and values
"""

def search_rotated_list(nums, value):
    """Method that returns the position of a value in a rotated sorted list"""
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        mid_value = nums[mid]

        if mid_value == value:
            return mid 

        # Determine which part of the list is sorted
        print(nums[lo])
        print(nums[hi])
        print(nums[mid])
        if nums[lo] <= mid_value:  # Left part sorted
            if nums[lo] <= value < mid_value: 
                hi = mid - 1
            else:  
                lo = mid + 1
        else:  # Right part sorted
            if mid_value < value <= nums[hi]: 
                lo = mid + 1
            else:  
                hi = mid - 1

    return -1  

nums = [4, 5, 6, 7, 0, 1, 2]
value = 0
result = search_rotated_list(nums, value)