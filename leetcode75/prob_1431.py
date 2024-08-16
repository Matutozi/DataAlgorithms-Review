"""
1431. Kids With the Greatest Number of Candies
"""

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """DO write a method that checks if u add extracandies to a particular student it causees student to have highest candy in list"""
        bool_list = []
        len_candies = len(candies)
        max_candy = max(candies)
        for i in range(len_candies):
            new_val = candies[i] + extraCandies
           
            if new_val >= max_candy:
                bool_list.append(True)
            else:
                bool_list.append(False)
            print("this is one go")
        return bool_list

candies = [2,3,5,1,3]
extraCandies = 3
ans_class = Solution()

ans = ans_class.kidsWithCandies(candies, extraCandies)
print(ans)