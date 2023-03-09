def combine(arr1, arr2):
    # answer array and two pointers that start at zero  
    ans = []
    i = j = 0

# loop that will run until one of the two pointers reach is the end of its array
# each iteration compares the elements
    while i < len(arr1) and j < len(arr2):
        # if element in array one is less than array two
        # it can be appeneded to answer and move forward
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        # OR it can be appended to second array and move
        # forward in this array
        # this should exhaust one of the two arrays
        else:
            ans.append(arr2[j])
            j += 1
    
    # code below ensures both list are exhausted
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans