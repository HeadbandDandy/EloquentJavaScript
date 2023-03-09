# will start at first and last index of string/array
# if first index is != to last then it will move 
# to left and to the right respectively for each index.
# while loop runs until the pointers match

def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True