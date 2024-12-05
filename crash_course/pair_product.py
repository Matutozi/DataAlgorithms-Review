"""
Code that finds the index of numbers that can multiply to give a value from a list
Use hashmap
complement = target_val/val_at_index
store the value and the index in the hash map with val=val , key=index
check if the current value is in the prev hash map, if it is present, return the two indexes

"""
def pair_product(numbers, target_product):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_product / num

        if complement in previous_numbers:
            return (index, previous_numbers[complement])
        
        previous_numbers[num] = index
