"""COde that implement the insertion sort"""

def insertion_Sort(nums):
    """Method that performs the insertion sort"""
    nums_copy = list(nums)

    for i in range(len(nums_copy)):
        j = i
        cur = nums_copy.pop(i)
        j = i - 1
        while j >= 0 and nums_copy[j] < cur:
            j-=1
        nums_copy.insert(j+1, cur)
    return nums_copy



#time complexity - O(n^2)


def new_insertion(nums):
    for i in range(len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums


nums = [1, 3,2,5,4,8,7,54,56,2,32]

print(new_insertion(nums))
print(insertion_Sort(nums))