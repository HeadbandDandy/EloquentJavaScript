import numbers


def linear_search(list, target): 
    # return the index position of the target if found
    # to make it through any list we need a for loop
    # Must return a value
    # Must be as expected
    
    for i in range(0, len(list)):
        # above is a constant time notation
        if list[i] == target:
            return i 
        return None 
    
def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else: 
        print("Target not found in list")
        
numbers = [x for x in range(10)]

result = linear_search(numbers, 12)
verify(result)



