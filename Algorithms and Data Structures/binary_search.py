# Constant time operation
# Logarithnmic run time
# with a redefined first and last the algo will run as many times as possible
# until it gets to a single element  

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        # calculate midpoint of list
        midpoint = (first + last)//2 # floor division operator // rounds down to nearest whole number
        # is value the same as we are looking for
        if list[midpoint] == target:
            return midpoint
        elif list [midpoint] < target:
            first = midpoint + 1
        else: 
            last = midpoint - 1
            
    return None 

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else: 
        print("Target not found in list")
        
numbers = [x for x in range(2000)]

result = binary_search(numbers, 12)
verify(result)
