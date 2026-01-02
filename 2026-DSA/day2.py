"""
Learning Record - Emmanuel Sobowale

LeetCode Practice: Two Sum Problem

- Problem: Given an array of integers `nums` and a target number, find two indices such that their values add up to the target.
- Strategy:
    - Introduced a dictionary `storage` to store numbers we've already seen along with their indices.
    - For each number, compute the complement (`target - nums[i]`) we need to reach the target.
    - Check if the complement exists in `storage`.
        - If yes, return the indices.
        - If no, store the current number with its index for future checks.
- Time Complexity: O(n), since we traverse the array only once.
- Space Complexity: O(n), for the dictionary storing seen numbers.

"""


def two_sum(nums, target):
    """
    Docstring for two_sum
    
    :param nums: num array
    :param target: target
    """
    
    compliment = 0
    storage = {}
    for i in range(len(nums)):
        compliment = target - nums[i]

        if compliment in storage:
            return [storage[compliment], i]
        
        else:
            storage[nums[i]] = i  

print(two_sum([1,2,3,4], 7))