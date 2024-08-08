def binary_search(lo, hi, condition):
    """method that implements the binary search"""
    while lo <= hi:
        middle = (hi + lo) // 2
        middle_val = condition(middle)

        if  middle_val == "found":
            return middle
        elif middle_val == "left":
            hi = middle - 1
        else:
            lo = middle + 1
    return -1


"""GIven an array of integers sorted in increasing order, find the starting and ending positon of a given number"""

def first_positon(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] > target:
            return "right"
        else:
            return "left"
        
    return binary_search(0,len(nums) -1, condition)

def last_potition(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums - 1) and nums[mid + 1] == target:
                return "right"
            else:
                return "found"
        elif nums[mid] < target:
            return "left"
        else:
            return "right"
        
    return binary_search(0, len(nums) - 1, condition)