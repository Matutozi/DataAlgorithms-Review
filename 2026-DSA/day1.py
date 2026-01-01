"""
Learning Record - Emmanuel Sobowale

Started with LeetCode 66, Plus One.
Further studies: tried implementing code for adding any number to the digits array.
- Introduced carry variable for multi-digit addition.
- Propagated carry digit by digit from right to left.
- Prepend carry if it remains after exhausting all digits.
- Practiced examples with multi-digit carry.
"""

def number_addition(array, k):
    """
    Docstring for number_addition
    
    :param array: Number Array
    :param k: Integer for Addition

    [1,2,4]
    k=5
    """

    #let carry be k
    carry = k
    for digit in range(len(array)-1, -1, -1):
        total = carry + array[digit]
        array[digit] = total % 10
        carry = total // 10 

    if carry > 0:
        array = [int(i) for i in str(carry)] + array

    return array

print(number_addition([1,2,4], 54))
    


