"""
Divide the input into two roughly equal parts
solve each part individually
combine the results to solve the problem for original inputs
include terminating conditions for small or invisible inputs

"""

def merge_sort(nums):
    if len(nums) <=1:
        return nums
    
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_numbers = merge(left_sorted, right_sorted)
    
    return sorted_numbers

def merge(nums1, nums2):
    merged = []

    i, j = 0, 0 #for iteration

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            merged.append(nums1[1])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail

#complexity - time and space - O(nlogn) , O(n )