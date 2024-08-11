"""for the quick sort 
pick a random element from the list called pivot
perform partioning(partition the array around the pivot element)
do the same steps as the merge sort algo recursuvvely call the partioned sections and join them
"""

def quick_sort(nums, start=0, end=None):
    """Method that performs quick sorting"""
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)

    return nums


def partition(nums, start, end):
    """Method that partitons the array"""
    start = 0
    end = len(nums) -1

    left, right = start, end - 1

    while right > left:
        if nums[left] <= nums[end]:
            left+= 1
        elif nums[right] > nums[end]:
            right -= 1

        else:
            nums[left], nums[right] = nums[right], nums[left]

    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end
    
