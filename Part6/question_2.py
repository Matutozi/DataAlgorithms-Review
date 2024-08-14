"""Given two strings A and B, find the numimum number of steps required to convert A to B, u can perform insert, deleter and replace
character
"""

str1 = "intention"
str2 = "execution"
output = 5

def min_steps(str1, str2):
    pass

"""
1. general case
2. no changes reqires
3. all characters need to be changed
4. equal length
5. unequal length
6. one string is empty
"""

def min_steps(str1, str2, i1= 0, i2=0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1+1, i2+1)
    else:
        return 1 + min(min_steps(str1, str2, i1+1, i2), min_steps(str1, str2, i1+1, i2+1), min_steps(str1, str2, i1, i2+1))
    


#adding memoissation
def min_edit_distance_memo(str1, str2):
    memo = {}
    def recursion(i1, i2):
        key = i1, i2
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str1[i1] == str2[i2]:
            memo[key] = recursion(i1 + 1, i2+1)
        else:
            memo[key] = 1 + min(recursion(i1+1, i2), recursion(i1+1, i2+1), recursion(i1, i2+1))

        return memo[key]
    return recursion(0,0)

ans = min_steps(str1, str2)
print(ans)

print(min_steps("", "int"))
