"""YOu are given an array of numbers, find a contious usbarrya of the list which adds up to a given sum"""

arr0 = [1,7,4,2,1,3]
target0 =  10
output= 2,6

def subarray_sum(arr, target):
    pass

"""
test cases
1. generic array where sub array is in center
2. sub array at start
3. sub array at end
4. no sub array that adds to 0
5. few zeros in list
6. multiple sub arrays in list
7. empty array
8. sub aray is a singe element
"""

#brute force solution O(n^3) time complexity
def brute_force_sum(array, targrt):
    n =len(array)
    for i in range(0,n):
        for j in range(i, n+1):
            if (sum(array[i:j]) == targrt):
                return i, j
            

    return None, None


ans = brute_force_sum(arr0, target0)
print(ans)


def subarray_sum(array, target):
    n = len(array)
    for i in range(0, n):
       sum = 0 #running sum
       for j in range(i, n+1):
           if sum == target:
               return i, j
           elif sum > target:
               break
           else:
               sum += array[j]

    return None, None

answer1 = subarray_sum(arr0, target0)
print(answer1)   