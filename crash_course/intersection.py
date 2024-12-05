"""Given two array, return a new array that contains elements that are common to the two arrays(their intersections)
iterate through the first array and compare it to elements in the second array -> brute force approach(too slow)
nested loops gives multipled time complexity
* use set() , store the elements in the first array in the set
iterate through the second array and compare if it is in set()

"""

def intersection(arr1, arr2):
    set_1 = set()
    set_1 = arr1
    new_array = list()

    for num in arr2:
        if num in set_1:
            new_array.append(num)

    return new_array




array1 = [1,2,3,4,5,6,7]
array2 = [2,4,6,8]

print(intersection(array1,array2)) #time complexity is O(n+m), space->O(n)
