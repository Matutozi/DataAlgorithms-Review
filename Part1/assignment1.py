"""Given a rotated sorted list that was rotated a number of times, we need to find the nuumber of times it was rotated
nums: a sorted list that is rotated [7, 9,3,5,6]
rotations: number of times the list was rotated ,2

"""

#express the test cases as dictionary
test = {
    "input": {
        "nums": [4,5,6,7,8,1,2,3]
    },
    "output": 5
}

#note that if a sorted list was rotated k times the smallest element is located at position K

"""USING LINEAR SEARCH
iterate througth the entire list and compare the two preceeding numnbers
if number is smaller than predecessor return the position 
else increment and repeat the steps
"""
def count_rotation_linear(nums):
    position = 1

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        
        position += 1
    return 0

"""
from jovian.pythondsa import evaluate_test_case
evaluate_test_case(count_rotation_linear, test)
#to test it out
"""

"""time complexity : O(N)
"""

"""USING BINARY SEARCH"""
def count_rotations_binary(nums):
    """method that implements the solution using binary search"""
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]

        if mid > 0 and mid_number < nums[mid - 1]:
            return mid
        
        if mid < len(nums) - 1 and nums[mid + 1] < nums[mid]:
            return mid +1
        
        if nums[mid] >= nums[lo]:
            lo = lo + 1

        else:
            hi = hi - 1
    return -1

from jovian.pythondsa import evaluate_test_case
evaluate_test_case(count_rotations_binary, test)


"""BINARY SEARCH METHOD THAT CAN HANDLE DUPLICATES"""

"""The method implemented below can handle duplicate values
    we would have a helper function that helps us perform the binary search"""
def binary_search(lo, hi, condition):
    """Method that performs the binary search"""

    while lo <= hi:

        mid = (lo + hi) // 2
        mid_number = condition(mid)

        if mid_number == "found":
            return mid
        elif mid_number == "left":
            hi = mid -1
        else:
            lo = lo + 1

    return -1 #try 0 also


def count_rotations_binary_dulicate(nums):
    lo = 0
    hi = len(nums) - 1

    def conditions(mid):
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return "found"
        if mid < len(nums) - 1 and nums[mid + 1] < nums[mid]:
            return "found"
        
        if nums[lo] == nums[hi] == nums[mid]:
            return "unsure"
        elif nums[lo] <= nums[mid]:
            return "right"
        else:
            return "left"
        
    rotation = binary_search(lo, hi, conditions)

    if rotation == 0:
        while lo< hi and nums[lo] == nums[hi]:
            lo += 1
            hi -+ 1
        rotation = binary_search(lo, hi, conditions)

    return rotation 
        




