"""Write a program to sort a group of numbers in asending order"""

def sort():
    pass

#dxample input snd outputs
test0 = {
    "input":{
        "nums":[4,2,6,3,4,6,2,1]
    },
    "output": [1,2,2,3,4,4,6,6]
}

tes1 = {
    "input":{
        "nums": [5,2,6,1,23,7,-12,12,-243,0]
    },
    "output": [-243,-12,0,1,2,5,6,7,12,23]
}

def bubble_sort(nums):
    """Method that implemts bubble sort"""
    nums_copy = list(nums)

    for _ in range(len(nums_copy) - 1):
        for j in range(len(nums_copy) - 1):
            if nums_copy[j] > nums_copy[j+1]:
                nums_copy[j], nums_copy[j+1] = nums_copy[j+1], nums_copy[j]

    return nums_copy

list_ =  [5,2,6,1,23,7,-12,12,-243,0]
sorted_l = bubble_sort(list_)
print(sorted_l)

#time complexity - O(n^2) - quadratic complexity
#space complexity - O(n)