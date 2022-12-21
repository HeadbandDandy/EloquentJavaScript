#  returns a true value instead of an indexed value
def recursive_binary(list, target):
    if len(list) == 0: 
        return False
    else:
        midpoint =(len(list))//2
        # searches for value
        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target:
                # creates a new list with a slice method
                return recursive_binary(list[midpoint +1:], target)
            else: 
                # only worries about from start up to midpoint
                return recursive_binary(list[:midpoint], target)
            
def verify(result):
    print("Target found: ", result)
    
    
numbers = [x for x in range(100)]

result = recursive_binary(numbers, 2122)
verify(result)