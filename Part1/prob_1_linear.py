#LINEAR SEARCH

def locate_card(cards, query):
    #use linear search algorithm(brute force solution)
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position #query found
        
        position += 1

        
    return -1 #query not found
        


#test case
cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3

result = locate_card(cards, query)
print(result) #expected output is 3

test = {
    "input": {
        "cards" : [13,11,10,7,4,3,1,0],
        "query" : 7
    },
    "output": 3
    
}

answer = locate_card(**test["input"]) == test["output"]
print(answer)
#dont forget the edge cases
"""
pip install jovian --upgrade --quiet
from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(locate_card, tests)"""

"""Complexity of algorithm
time complexity : O(n)
space complexity : O(1)
"""
