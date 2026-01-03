"""
    Started with the LeetCode problem `repeatedNTimes`.
        Further studies: modified the code to handle a general case 
        of finding the number with the largest occurrence in a list.

        - Used a dictionary to count occurrences of each number.
        - Introduced 'largest_count' to track the highest frequency.
        - Introduced 'largest_num' to track the corresponding number.
        - Compared each number's frequency with 'largest_count' as we iterate.
        - Returned 'largest_num' at the end of the iteration.
        - Handles ties by returning the first number to reach the highest frequency.
"""


class Solution:
    def repeatedNTimes(self, nums) -> int:
        """
        Docstring for repeatedNTimes
        
        :param nums: List of integers
        :return: Integer that appears most frequently
        :rtype: in
        """

        dict_array = {}
        largest_count = 0
        largest_num = None
        
        for num in nums:
            if num not in dict_array:
                dict_array[num] = 1
    
            else:
                dict_array[num] += 1
            
            if dict_array[num] > largest_count:
                largest_count = dict_array[num]
                largest_num = num

        return largest_num
            
[1, 2, 2, 3, 3, 3]
