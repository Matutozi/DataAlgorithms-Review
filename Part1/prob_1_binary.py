#BINARY SEARCH
"""find the middle of the list
if mastch found, return the middle position
if less than queried number sesearch the first half of list or vice versa
"""

def test_location(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 > 0 and cards[mid-1 ] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"
    
def locate_card(cards, query):
    #find the middle of list
    length = len(cards)
    
    low = 0
    high = length - 1

    while low <= high:
        middle = (high + low) // 2
        mid_number = cards[middle]
        result = test_location(cards, query, middle)
        #print(result)

        if result == "found":
            return middle
        elif result == "left":
            high = middle - 1
        elif result== "right":
            low = middle + 1
    return -1

tests = [
    {
        "input": {
            "cards": [13, 11, 10, 7, 4, 3, 1, 0],
            "query": 7
        },
        "output": 3
    },
    # Single element list where the element is the query
    {
        "input": {
            "cards": [7],
            "query": 7
        },
        "output": 0
    },
    # Single element list where the element is not the query
    {
        "input": {
            "cards": [7],
            "query": 5
        },
        "output": -1
    },
    # Empty list
    {
        "input": {
            "cards": [],
            "query": 7
        },
        "output": -1
    },
    # List with repeated elements where the query is in the middle
    {
        "input": {
            "cards": [13, 11, 10, 7, 7, 7, 4, 3, 1, 0],
            "query": 7
        },
        "output": 3
    },
    # List with repeated elements where the query is at the start
    {
        "input": {
            "cards": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            "query": 7
        },
        "output": 0
    },
    # List with repeated elements where the query is at the end
    {
        "input": {
            "cards": [10, 10, 10, 10, 7, 7, 7],
            "query": 7
        },
        "output": 4
    },
    # List where the query is not present
    {
        "input": {
            "cards": [10, 9, 8, 6, 5, 4, 2, 1],
            "query": 7
        },
        "output": -1
    },
    # List where all elements are the same and equal to the query
    {
        "input": {
            "cards": [7, 7, 7, 7, 7, 7, 7],
            "query": 7
        },
        "output": 0
    },
    # List where all elements are the same and not equal to the query
    {
        "input": {
            "cards": [7, 7, 7, 7, 7, 7, 7],
            "query": 10
        },
        "output": -1
    }
]
    

from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(locate_card, tests)
#to test it out
